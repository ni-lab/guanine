# GUANinE

```
   _____  _    _           _   _  _         ______ 
  / ____|| |  | |   /\    | \ | |(_)       |  ____|
 | |  __ | |  | |  /  \   |  \| | _  _ __  | |__   
 | | |_ || |  | | / /\ \  | . ` || || '_ \ |  __|  
 | |__| || |__| |/ ____ \ | |\  || || | | || |____ 
  \_____| \____//_/    \_\|_| \_||_||_| |_||______|
```
                                                   
### %% Under Development %% 

Our temporary submission method is via uploading test-set predictions to a Google form: [https://forms.gle/NhYSwH3Rjn3ShRzQ7](https://forms.gle/NhYSwH3Rjn3ShRzQ7)

We will be launching an automatic evaluation server at a later date


## Intro
The GUANinE benchmark for genomic AI uses the [Hugging Face](https://huggingface.co/) API for dataset loading. **We are in the process of creating dataloading scripts for each dataset, so at the moment you'll need to clone the task repository and manually load the data.** GUANinE uses predetermined splits for each task, with private test set labels for our leaderboard (Coming soon!).  

See the available datasets here: [https://huggingface.co/guanine](https://huggingface.co/guanine) 

### Download a task
```bash
git clone https://huggingface.co/datasets/guanine/[TASK_NAME]

## e.g. 
git clone https://huggingface.co/datasets/guanine/dnase_propensity 
ls dnase_propensity
## 1per bed dev test train

```  

## Load a task 
Once dowloaded, there are two separate copies of each task -- CSV and BED. The CSV has a fixed-length (509-512 bp) context included, which makes it *much* larger than the BED files. The BED files are tab-delimited and contain the chromosomal coordinate start, end, and *center*. For large-context models, e.g. Basenji2, we would recommend using the BED files and manually extracting sequence data from hg38.

### 1) Install twobitreader to load hg38 sequences:
```bash
pip install twobitreader
wget -nc https://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/hg38.2bit
```
### 2) Extract a sequence in Python 
```python
import pandas as pd
import twobitreader

train_bed = pd.read_csv('dnase_propensity/bed/train/train.bed', sep='\t')

# extract 2,000 bp around the first example
width  = 2000 
chr    = train_bed.iloc[0]['#chr']
center = train_bed.iloc[0]['center']  
start  = center - width//2
end    = center + width//2

hg38   = twobitreader.TwoBitFile('hg38.2bit')
sequence = hg38[chr][start:end]
print(chr, center, train_bed.iloc[0]['y'], sequence)
## chr2 205691090 1 TAACCAGTAAC...
```
## Baseline Model Usage 

We are in the process of uploading our T5 baseline models, pretrained and unpretrained. For models that are not pretrained with span corruption (language modeling), the default branch of each model is our dnase-propensity task. 

```python 
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# load the input tokenizer and trained model on a CPU
tokenizer = AutoTokenizer.from_pretrained("guanine/t5_baseline")
model = AutoModelForSeq2SeqLM.from_pretrained("guanine/t5_baseline")

# load the output tokenizer and perform a prediction 
output_tokenizer = AutoTokenizer.from_pretrained("guanine/t5_regression_vocab")
inputs = tokenizer('TCGATCGATCGATCGA', return_tensors='pt') 
decoder_input_ids = torch.tensor([[0]]) # required for decoding outputs

# inference w/o gradients
with torch.no_grad():
  out = model(**inputs, decoder_input_ids=decoder_input_ids)
  logits = out['logits']

# predictions is a string, T5 models by default is a text-to-text transformer 
predictions = output_tokenizer.decode(logits.argmax().numpy().tolist())

```

To access a model trained on a different task, use 
```python
# revision is one of main, ccre_propensity, cons30, cons100, gpra_c, and gpra_d
model = AutoModelForSeq2SeqLM.from_pretrained("guanine/t5_baseline", revision='ccre_propensity')
```



