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

### We will be providing details on how to score your predictions on the test set shortly



