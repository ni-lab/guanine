======================
ccre_propensity
======================

 | tags: candidate cis-Regulatory Elements, cCREs, Histone Marks, DHS, functional genomics, sequence function, reference sequences, experimental measurements

tl;dr
------ 
``ccre_propensity`` (aka ``ccre_prop``) is a multitask dataset of epigenetic markers for functional elements in the human genome. Models fit to one or all subtask(s) in ``ccre_prop`` should be able to 'tag' sequences containing functional elements, i.e. DNA sequences that do something *other* than "get turned into proteins." 

overview
--------
candidate Cis-Regulatory Elements, or cCREs, are a spectrum of genome annotations that represent genomicists' mapping of sequence elements, e.g. promoters, or DNA segments that increases downstream transcription. `By design`_, cCREs transcend cell types -- a cCRE in one tissue type is still present in another tissue type, even if its regulatory logic is left dusty and unused. The `ENCODE`_ registry of cCREs are based on where epigenetic signals -- typically histone marks -- are found across the human reference genome ``hg38``. 

|

This epigenetic signal allows for functional labels to be assigned to a sequence of DNA, be it promotor, enhancer, structural CTCF site, or even just a DNase Hypersensitive Site (DHS -- an ingredient in all cCREs). It was created from the `SCREEN v2`_ database, itself a subset of the ENCODE_ project. Sequence labels :math:`y` correspond to the likelihood an *accessible* sequence would be annotated as having H3K4me3 or H3K27ac histone marks, CTCF-binding properties, or DNase hypersensitivity (DNase). Unlike typical cCRE tracks, which only measure experimental outcomes in a single cell line or cell type, cCRE is cell-type-agnostic and corresponds to *basal* tendency, or propensity, to be functional across cell types. ``ccre_prop``, like its *unconditional* counterpart, ``dnase_propensity``, is cell-type-agnostic, but cell-type-specific models will likely still perform well on this task due to the nature of its construction. 

|

The high-level statistical model is :math:`y_H \sim p(H \ | \ X, \textrm{DHS})` for :math:`H` a given epigenetic signal and :math:`X` a DNA sequence that is presumed accessible (i.e. a DHS). There are four signals used in ``ccre_prop``, one per each subtask, the scores of models are averaged into a single combined score -- subscores are often reported in appendices or omnibus tables as ccre-*H*, e.g. ccre-H3K4me3. Note that the loci in ``ccre_prop`` are a **strict subset** of loci in the ``dnase_propensity`` task, since a site must be accessible to be considered a candidate CRE in Encode/SCREEN. 

|

Class labels are **ordinal** and range from zero (0, no epigenetic signal) to four (4, nearly ubiquitous epigenetic signal across cell types). Intermediate scores of one to three (1-3) represent some degree of cell-type-specific signal, although the type of cells is left unsaid. 

**warning**: Models trained to predict ccre_prop may not be well-behaved on inaccessible sequences, since only DHS sequences are seen during training. To use the predictions of ccre_prop-trained models, one should first condition their output on the result of ``dnase_propensity`` models or similar measures of accessibility. 

interpretation
--------------
``ccre_prop`` is a core indicator of sequence function, and models scoring well on it must at least recognize, if not comprehend, regulatory functional elements in the reference genome. That said, while ``ccre_propensity`` corresponds to the *degree* of cell-type-specific epigenetic signal, it does not indicate *which* cell types a sequence is functional in, nor can it measure a model's ability to predict any specific cell type's H3K4me3, H3K27ac, CTCF, or DHS tracks.

|

Additionally, while Cis-Regulatory elements are indicative of sequence function, a model that can predict ``ccre_prop`` is not guaranteed to understand their cell-type-specific implications, or to *understand* the impact of sequence or epigenetic perturbations (e.g. variant effects, CRISPR knockout effects). 

|

Supervised models like DeepSEA, Enformer, Borzoi, etc, are prime examples of models built for ``ccre_prop`` -- their own training data includes the same H3K4me3, H3K27ac, CTCF, and DHS tracks that make up ``ccre_prop``. To restate, ``ccre_prop`` is *in-distribution* for supervised models trained on ENCODE egigenetic tracks, and those that score below 100 should be understood as having underfit their training data. 

|

The most closely related task is `dnase_propensity`_, which measures the accessibility ingredient of Cis-Regulatory Element functionality (by definition, `see ENCODE v3`_). Finally, one can understand the difference between ``dnase_propensity`` and ``ccre-dnase`` to be the likelihood of a sequence :math:`X` being accessible versus its degree of accessibility (conditioned on being accessible), although this is a loose relationship. 

build details 
-------------
Basal epigenetic signal is approximated by integrating out cell-type-specific signal, i.e. :math:`\int_{c \in C} \ p(H \ | \ X, \textrm{DHS}, c)` for :math:`c` a given cell-type. Specifically, for the over 1600 cCRE tracks in `SCREEN v2`_, the same tracks used to train DeepSEA, Enformer, etc, we consider the discrete summation :math:`y_H(X) \propto \sum_{t \in \textrm{H-cCRE tracks}} \ \alpha_t \ \cdot \ \textbf{1}_\textrm{H-cCRE}(X)` for boolean indicator function :math:`\textbf{1}_\textrm{H-cCRE}(X)`, which can be decomposed into constituent indicator functions :math:`\textbf{1}_\textrm{H-cCRE}(X) = \textbf{1}_\textrm{H}(X) \ \cdot \ \textbf{1}_\textrm{DHS}(X)`, where both components represent boolean consensus peak-calling for the underlying tracks. Note this implies that :math:`\textbf{1}_\textrm{H-cCRE}(X)` is **undefined** for cells lacking either signal -- far fewer types (still several hundred per task) of cells are included in the construction compared to ``dnase_propensity``. 

|

Also note the weighting :math:`\alpha_t`, which allows us to downweight cancerous cell lines by half (to help mitigate cancer-specific epigenetic signals). 

|

Because `SCREEN v2`_ relies on *consensus* peak calling, the peak called loci for reference sequences is consistent across tracks, which allows for this otherwise difficult function to be well-defined.

|

Finally, for ease of modeling, the raw :math:`y_H(X)` scores are binned from one to four (1-4), and a partially G/C-balanced *control* set of accessible sequences (i.e. from ``dnase_propensity``) are added to the dataset with labels of zero (0). 

controlled factors
-------------------
- repetitive elements (partial)
- G/C content (partial)
- immortalized cancer line accessibility (partial) 


appears in
---------------- 
`GUANinE v1.0`_

|

.. _`dnase_propensity`: ./dnase_propensity.html
.. _`By design`: https://www.nature.com/articles/s41586-020-2493-4
.. _`see ENCODE v3`: https://www.nature.com/articles/s41586-020-2493-4
.. _`GUANinE v1.0`: https://proceedings.mlr.press/v240/robson24a.html 
.. _`SCREEN v2`: https://screen.encodeproject.org/
.. _`ENCODE`: https://www.encodeproject.org/
