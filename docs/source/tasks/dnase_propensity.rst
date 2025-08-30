======================
dnase_propensity
======================

 | tags: DNase hypersensitive sites, DHS, accessibility, functional genomics, sequence function, reference sequences

tl;dr
------ 
``dnase_propensity`` (aka ``dnase_prop``) measures the tendency of a DNA sequence to be accessible, i.e. cut or cleaved by the DNase enzyme. Unlike the typical concept of a DNase Hypersensitive Site (DHS), this propensity, or disposition, is agnostic to cell-types and instead measures *basal* sequence accessibility across tissues and organs. 

overview
--------
For a DNA sequence to function, it cannot be densely packed away in closed chromatin -- it must be 'unpacked,' i.e. accessible. The simplest measure of 'unpackedness' is a sequence's ability to be digested by a DNase enzyme, which naturally slices up any 'loose' DNA. The idea that certain regions of the genome are regularly, if not always, accessible lead to the idea of (functional) *elements* being located in "DNase-hypersensitive" positions across the genome, hence the task's name. 


``dnase_prop`` was constructed on the human reference genome ``hg38`` based on a combination of DHS tracks from the `SCREEN v2`_ database, a subset of ENCODE_. Sequence labels :math:`y` correspond to the likelihood a sequence would be annotated as accessible (a DHS) -- an essential indicator of sequence function. Although ``dnase_prop`` is cell-type-agnostic, cell-type-specific models will perform well on this task due to the nature of its construction. The high-level statistical model is :math:`y \sim p(\textrm{DHS} \ | \ X)` for :math:`X` a given DNA sequence. 


Class labels are **ordinal**, i.e. represent a ranking, and they range from zero (0, completely inaccessible) to four (4, almost always accessible, at least across measured cell-types). intermediate scores of one to three (1-3) represent some degree of cell-type specific accessibility, although which types of cells is left unsaid. 

interpretation
--------------
Accessibility is one of the most fundamental features of sequence function, and models scoring well on ``dnase_prop`` likely recognize functional genomic elements (including cis-regulatory elements) in the reference genome. That being said, while it corresponds to the *degree* of cell-type-specific accessibility, it does not indicate *which* cell types a sequence is accessible in, nor does it directly measure a model's ability to predict a specific cell type's DHS track.


Additionally, while accessibility suggests sequence function, a model that can predict ``dnase_prop`` is not guaranteed to possess functional element *understanding*; such a model may not be able to infer sequence function in the reference genome (including function indicated by histone marks, e.g. H3k4me3 for sequence promoters), much less be able to estimate the effects of variants. 


Supervised models like DeepSEA, Enformer, Borzoi, etc, are prime examples of models built for ``dnase_prop`` -- their own training data includes the same DHS tracks that make up ``dnase_prop``. To restate, ``dnase_prop`` is *in-distribution* for supervised models trained on ENCODE DHS tracks, and a score below 100 should be understood as having underfit their training data.


.. tip:: The most closely related task is `ccre_propensity`_, which builds on top of dnase_prop's measure of accessibility to assess sequence function. 


build details 
-------------
Basal accessibility is approximated by integrating out the signal unique to cell types, i.e. :math:`\int_{c \in C} \ p(\textrm{DHS} \ | \ X, c)` for :math:`c` a given cell line or cell type. Specifically, for the over 700 DHS tracks in `SCREEN v2`_, we consider the discrete sum :math:`y(X) \propto \sum_{t \in \textrm{DHS tracks}} \ \alpha_t \ \cdot \ \textbf{1}_\textrm{t, DHS}(X)` for boolean indicator function :math:`\textbf{1}_\textrm{t, DHS}(X)`, which represents the signal at the locus of sequence :math:`X` being called as a peak (1) or non-peak (0) in typical DHS-track fashion. Of note is the weighting :math:`\alpha_t`, which allows us to downweight cancerous cell lines by half (to help mitigate cancer-specific accessibility signals). 


Because `SCREEN v2`_ makes use of *consensus* peak calling, the peak-called loci for reference sequences is the same across tracks -- this allows for an otherwise difficult-to-pinpoint function to be well-defined.


Finally, for ease of modeling, the raw :math:`y(X)` scores are binned from one to four (1-4), and a partially G/C-balanced *control* set of inaccessible sequences are added to the dataset with labels of zero (0). 

controlled factors 
-------------------
- repetitive elements (partial)
- G/C content (partial)
- immortalized cancer line accessibility (partial) 


appears in
---------------- 
`GUANinE v1.0`_

| 

.. _`ccre_propensity`: ./ccre_propensity.html
.. _`GUANinE v1.0`: https://proceedings.mlr.press/v240/robson24a.html 
.. _`SCREEN v2`: https://screen.encodeproject.org/
.. _`ENCODE`: https://www.encodeproject.org/
