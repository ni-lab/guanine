======================
cons100
======================

 | tags: conservation, multiple sequence alignment, MSA, deleteriousness, mammalian genomes, mammals, phyloP, phyloP100way

tl;dr
------ 
cons100 (aka cons100_binned) is a sequence conservation annotation task, which asks a model to identify (ultra-)conserved elements that have evolved under negative selection. Regions that have experienced selection are almost certainly functional (or close to regions that are).

overview
--------
Conservation signal, typically measured as the proportion of bases that are (near-)constant in a multi-organismal multiple sequence alignment, is a fantastic proxy for sequence function -- and doesn't require costly experimental annotation. Here, conservation signal is defined as region-level average across 512 base pairs using the single-bp-resolution `phyloP100way`_ score, which is built on MSAs of vertebrate genomes, mostly mammalian, to the human reference genome (spanning speciation from 500~ MYA to present).  This gives the task a relaxed representation of conserved elements, as it's far more continuous than a boolean conserved/unconserved label. 

The approximate statistical model is :math:`y_{\{X_1 \ldots X_{512} \}} \sim \frac{1}{512}\sum_{i=1..512} p(X_i)` for a tendency to evolutionary stasis :math:`p(X_i)` (higher is more conserved, lower is rapidly changing). 

Class labels are **ordinal** and range from zero (0, unconserved) to twenty-four (24, highly conserved). Intermediate scores represent moderate amounts of average bp-level sequence conservation, possibly at a gene boundaries or less-conserved sequence. 

.. note:: 
    Conservation is deeply connected to deleteriousness and pathogenicity, but this task, while helpful in identifying functional elements, ignores individual variation because it measures deleteriousness at evolutionary scale. Mutational 'constraint' is a complementary metric that uses population-level data to emulate conservation through observed individual variation.

example models 
--------------
========================  ============
model                     :math:`\rho`
========================  ============
nt-v2-500m                **63.5168**
Enformer (Pre-output)     62.4178
Caduceus-PS               62.3797
Enformer                  62.2344
Evo2_7B_base              61.8923
5-mer LinSVR (baseline)   36.3022
GC-content  (baseline)    20.5533
========================  ============

interpretation
--------------
With the advent of the first human and non-human reference genomes, multiple sequence alignment (MSA) approaches for functional element detected surpassed (and largely displaced) ORF detectors and other traditional feature-based models of sequence function, due in part to the simplicity of MSAs' construction, versatility, and potent use of slight-supervision (alignments). `phyloP100way`_ distills a column's worth of MSA information into a single score, which permits straightforward comparison between individual base pairs, elements, and even regions through their phyloP representations. 


Language models like DNABERT-2, Nucleotide Transformer, Caduceus, etc are ideal for modeling conservation tasks like cons100, since the implicit cloze-completion behavior of language modeling requires some portion of the sequence to be predictable, i.e. static and unchanging. Track-supervised models like DeepSEA, Enformer, Borzoi, etc, also tend to perform well -- especially with higher context sizes -- due both to a tacit comprehension of local regulatory grammar as well as so much of negative selection being *contextual*, e.g. proximity of a "conserved" region to an actually loss-of-function intolerant ultra-conserved gene or *micro*\chromosomes having fewer intergenic regions, complicating recombination. For more details (as well as limitations to phyloP), one should consult `McVicker et al. (2009)`_ and also perhaps review vertebrate chromosomal evolution, e.g. `Waters et al. (2021)`_. 


The most closely related task is `cons30`_, which is a similar task built with smaller, more human-proximal (evolutionarily) genomes.


Finally, one can understand the difference between cons30 and cons100 to represent some indicate degree of overfitting/specialization to primate or mammalian genomes, as the former is more evolutionarily proximal to humans. Enformer, Borzoi, et al, having been trained on both human and mouse genomes, tend to perform comparatively poorly on cons100 partly because of this specialization. 

example usage
-------------
first, clone the dataset from huggingface (make sure you have ``Git LFS`` installed): ::

    git clone https://huggingface.co/datasets/guanine/cons100

then, read the file into main memory with your favorite file parser

.. code-block:: python
   :caption: loading with pandas

   import pandas as pd

   # 1per is the recommended few-shot training split
   train_dat = pd.read_csv('cons100/bed/1per/1per.bed', sep='\t')
   train_dat.head()

finally, splice the sequence out with your preferred genome reader, e.g. ``twobitreader``

.. code-block:: python
   :caption: accessing sequences with twobitreader

   from twobitreader import TwoBitFile

   # download from https://hgdownload.cse.ucsc.edu/goldenpath/hg38/bigZips/hg38.2bit
   hg38 = TwoBitFile('hg38.2bit')

   CONTEXT_SIZE = 8192 # change this for your model

   row = train_dat.iloc[0]
   ch = row['#chr'] ## fun fact -- conservation varies greatly by chr size 
   st = row['center']-CONTEXT_SIZE//2
   en = row['center']+CONTEXT_SIZE//2

   seq = hg38[ch][st:en] 

   # optionally convert your sequence to uppercase before tokenizing it, etc
   seq = seq.upper() 
   assert len(seq)==CONTEXT_SIZE # we recommend checking for truncation


build details 
-------------
Per-bp-level evolutionary stasis (negative selection) is approximately formulated as :math:`p(X_i) \propto  \Phi^{-1}(1 - h_{MSA}(X_{i}))` with :math:`\Phi^{-1}` the gaussian quantile function and :math:`h_MSA` the *expected* rate of evolutionary substitution (0-1) for genome sequence :math:`X` at position :math:`i`. As an example, if position :math:`i` is mostly identical across an MSA, one could *expect* position :math:`i` to have a low value of :math:`h_{MSA}`, indicating strong negative selection, and thus a highly positive :math:`p(X_i)`. One should consult the original `phyloP`_ paper for a non-handwavey definition. 

A rank transformation is applied to quantize (and rectify) the :math:`y` values, with each bin corresponding to :math:`\sim 4\%` of sequences.

Human accelerated regions were removed from the task before quantization by pruning noisy regions (those with high coefficients of variation).

controlled factors
-------------------
- human accelerated regions (moderate)
- repetitive elements (moderate)
- unaligned regions (significant) 


appears in
---------------- 
`GUANinE v1.0`_

original citation
-----------------

Pollard KS, Hubisz MJ, Siepel A. Detection of non-neutral substitution rates on mammalian phylogenies. Genome Res. 2010 Jan;20(1):110-21. (http://genome.cshlp.org/content/20/1/110.long)

|

.. _`cons30`: ./cons30.html
.. _`Waters et al. (2021)`: https://pmc.ncbi.nlm.nih.gov/articles/PMC8609325/
.. _`McVicker et al. (2009)`: https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1000471
.. _`phyloP`: https://pmc.ncbi.nlm.nih.gov/articles/PMC2798823/
.. _`phyloP100way`: https://hgdownload.soe.ucsc.edu/goldenPath/hg38/phyloP100way/
.. _`GUANinE v1.0`: https://proceedings.mlr.press/v240/robson24a.html 
.. _`SCREEN v2`: https://screen.encodeproject.org/
.. _`ENCODE`: https://www.encodeproject.org/