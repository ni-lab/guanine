======================
dnase_propensity
======================

 | tags: DNase hypersensitive sites, DHS, accessibility, functional genomics, sequence function, reference sequences

tl;dr
------ 
dnase_propensity (aka dnase_prop) is a measure of basal sequence accessibility on hg38 (human reference) sequences. it was created from the `SCREEN v2`_ dataset, itself a subset of ENCODE_ ROADMAP v3. Sequence labels :math:`y` correspond to the likelihood (or disposition) a sequence would be annotated as a DNase Hypersensitive Site (DHS) -- an essential marker for sequence function. dnase_prop is cell-type-agnostic, but cell-type-specific models will likely still perform well on this task due to the nature of its construction. 

|

The approximate statistical model is :math:`y \sim p(\textrm{DHS} \ | \ X)` for :math:`X` a given DNA sequence. 

|

Class labels are **ordinal** and range from zero (0, completely inaccessible) to four (4, almost always accessible, at least across measured cell-types). intermediate scores of one to three (1-3) represent some degree of cell-type specific accessibility, although which types of cells are uncertain. 

interpretation
--------------
dnase_prop is one of the most fundamental features of sequence function, and models scoring well on it likely recognize accessible elements (including cis-regulatory elements) in the reference genome. That being said, while it corresponds to the *degree* of cell-type-specific accessibility, it does not indicate *which* cell types a sequence is accessible in, nor can it measure a model's ability to predict any specific cell type's DHS tracks.

|

Additionally, while accessibility underpins sequence function, a model that can predict dnase_prop is not guaranteed to possess functional element *understanding*; such a model may not be able to estimate sequence function (indicated by histone marks, e.g. H3k4me3 for sequence promoters) in the reference genome, much less be able to articulate variant effects. 

|

Supervised models like DeepSEA, Enformer, Borzoi, etc, are prime examples of models built for dnase_prop -- their own constituent training data includes very same (possibly normalized) DHS tracks that make up dnase_prop. To restate, dnase_prop is *in-distribution* for supervised models trained on ENCODE DHS tracks, and those that score well below 100 should be understood as having underfit their training data. 

|

The most closely related task is ccre_propensity (link), which builds on top of dnase_prop's gauge of sequence accessibility to begin to access sequence functionality. 


build details 
-------------
Basal accessibility is approximated by integrating out cell-type-specific signal, i.e. :math:`\int_{c \in C} \ p(\textrm{DHS} \ | \ X, c)` for :math:`c` a given cell-type. Specifically, for the over 700 DHS tracks in `SCREEN v2`_, the same tracks used to train DeepSEA, Enformer, etc, we consider the discrete summation :math:`y(X) \propto \sum_{t \in \textrm{DHS tracks}} \ \alpha_t \ \cdot \ \textbf{1}_\textrm{DHS}(X)` for boolean indicator function :math:`\textbf{1}_\textrm{DHS}(X)`, which signifies whether the signal at the loci corresponding to sequence :math:`X` was called as a peak or non-peak in typical DHS track fashion. Of note is the weighting :math:`\alpha_t`, which allows us to downweight cancerous cell lines by half (to help mitigate cancer-specific accessibility signals). 

|

Because `SCREEN v2`_ relies on *consensus* peak calling, the peak called loci for reference sequences is consistent across tracks, which allows for this otherwise difficult function to be well-defined.

|

Finally, for ease of modeling, the raw :math:`y(X)` scores are binned from one to four (1-4), and a partially G/C-balanced *control* set of inaccessible sequences are added to the dataset with labels of zero (0). 

controlled factors: 
-------------------
- repetitive elements (partial)
- G/C content (partial)
- immortalized cancer line accessibility (partial) 


appears in
---------------- 
GUANinE v1.0

|



.. _`SCREEN v2`: https://screen.encodeproject.org/
.. _`ENCODE`: https://www.encodeproject.org/