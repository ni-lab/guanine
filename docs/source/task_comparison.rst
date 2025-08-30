=========================
Differences between tasks
=========================

Like any general-purpose benchmark, ``GUANinE`` has multiple tasks for evaluating model performance across domains, perspectives, and applications. Below, we compare and contrast the actual tasks, but first, let's refresh our memories about the meaning of "task" the types of tasks we encounter in genomes.

Background
----------
We'll start by saying a model :math:`M` exhibits task performance :math:`T = R(M, D)` for a performance function :math:`R` and dataset :math:`D`.  A "learning" machine (in the abstract sense) is one that can achieve :math:`T_2 > T_1` after processing said dataset `D`.

.. tip::

  ``GUANinE`` tries to simplify the many choices of :math:`R` by relying on Spearman's :math:`\rho` (pronounced *rho*), so don't worry too much about that for now.   


As with anything in genomics, ``GUANinE``'s tasks can be split into two categories: Annotation and Perturbation.

Annotation Tasks
----------------
Annotation broadly characterizes a sequence, focusing on what makes it unique compared to other sequences. While not always considered 'exciting,' annotation tasks are the **core** performance measure of a successful model. If a model cannot *recognize* a gene, it's almost certainly not going to understand what happens when you try to *change* said gene. ::

  `dnase_propensity`_: 
    Measures the accessibility of a sequence, i.e. its tendency to be accessed cellular machinery like transcription factors. It's a great proxy for a "functional" sequence.
  
  `ccre_propensity`_: 
    Imputes the nature of an accessible sequence  -- is it a promoter? an enhancer? What histone marks might it have? 
  
  `cons30`_:
    Assesses the 'conservation' of a sequence -- do other mammals have this same sequence? It's almost certainly functional if it's shared and experiences natural selection.
  
  `cons100`_:
    Similar to cons30, but on the broader family of vertebrates. If a sequence has a high cons100 score, you know it's as old as the dinosaurs ;) 

Perturbation Tasks
------------------
Pertubration tries to figure out what makes a sequence 'tick' by poking or prodding it (chemically). These tasks don't necessarily 'build' on Annotation tasks, but it's fair to say they're the more difficult tasks -- and require far greater precision. The most infamous Perturbation tasks tend to be variant effect tasks, i.e. predicting what happens when a single nucleotide in a sequence is altered. ::

  `gpra_c`_:
    The first of the two large-scale gene expression tasks based on dual-reporter assay of randomized promoters in yeast (i.e. more diverse than natural sequences).  
  
  `gpra_d`_:
    The second of the two. It's not redundant redundant! It's an excellent sanity check and could make for an awfully nice transfer learning paper \*hint, hint; wink, wink\*.
  
  `cadd_snv`_:
    \*THE\* synthetic variant interpretation task, and one of the best training datasets for SNV models to-date. If you want to predict deleteriousness or rare variants in humans, start here. 

  `clinvar_snv`_:
    A heavily sanitized & balanced noncoding pathogenicity dataset for scoring variant models. It's small, but that just means its quality is higher. 
  

.. _`dnase_prop`: ./tasks/dnase_propensity.html
.. _`ccre_prop`: ./tasks/ccre_propensity.html
.. _`cons30`: ./tasks/cons30.html
.. _`cons100`: ./tasks/cons100.html
.. _`gpra-c`: ./tasks/gpra_c.html
.. _`gpra-d`: ./tasks/gpra_d.html
.. _`cadd-snv`: ./tasks/cadd_snv.html
.. _`clinvar-snv`: ./tasks/clinvar_snv.html