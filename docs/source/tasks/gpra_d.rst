======================
gpra-d
======================

 | tags: gene expression, promoter sequences, GPRA, dual-reporter assay, yeast, synthetic biology

tl;dr
------ 
``gpra-defined`` (aka ``gpra-d``) is a synthetic biology task measuring gene expression in yeast. ``gpra-d`` solves the issue of finite natural gene-promoter diversity by relying on random oligonucleotides. 

overview
--------
The central dogma suggests that genes exist to produce RNA, which is then used to manufacture proteins. Upstream promoter elements heavily regulate the amount of RNA a gene can produce, known as its gene *expression*. Because genes (and their adjacent promoters) tend to be constrained evolutionarily, there is limited sequence diversity in and around gene regions -- including promoters. This means that only a small, finite set of  promoter sequences (~ 20k in hg38) are 'trainable' for any given model. To circumvent this bottleneck, the `de Boer lab`_ has developed ways of injecting randomized promoter sequences (complete with their own control) into yeast, known as Gigantic Parallel Reporter Assays.

Class labels are **ordinal** and range from zero (0, minimal expression) to seventeen (17, maximal expression). Intermediate scores of one to sixteen (1-16) represent increasing levels of gene expression. 

.. seealso:: The sibling task `gpra-c`_ is intended to allow transfer learning research -- but both are sizeable stand-alone tasks. 

interpretation
--------------

``gpra-d`` is an insightful task with across-the-board higher performance nubmers compared to ``gpra-c`` (typically a consistent +4 delta). While its dynamic range (the typical upper and lower bound of scores) is slightly constrained -- it nonetheless produces rankings that correlate to model quality and other tasks (i.e. the newest, fanciest models increasingly do well). 

build details 
-------------
Compared to the source dataset, ``gpra-d`` has undergone slight refinement. Specifically, non-canonical length datapoints (i.e. those differening from the standard 80 bp of randomized sequence) have been pruned. While the variability in length likely represents some biological signal, it trivialized a significant portion of the final scoring (as non-80 lengths clustered heavily across the class labels).

controlled factors 
-------------------
- sequence length


appears in
---------------- 
`GUANinE v1.0`_

|

.. _`gpra-c`: ./gpra_c.html
.. _`GUANinE v1.0`: https://proceedings.mlr.press/v240/robson24a.html 
.. _`de Boer Lab`: https://github.com/de-Boer-Lab
