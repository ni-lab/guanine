=========================
Differences between tasks
=========================

Like any general-purpose benchmark, ``GUANinE`` has multiple tasks for evaluating model performance across domains, perspectives, and applications. Below, we compare and contrast the actual tasks, but first, let's refresh our memories about the meaning of "task" the types of tasks we encounter in genomes.

Background
----------
We'll start by saying a model :math:`M` exhibits task performance :math:`T = R(M, D)` for a performance function :math:`R` and dataset :math:`D`.  A "learning" machine (in the abstract sense) is one that can achieve :math:`T_2 > T_1` after processing said dataset `D`.

``GUANinE`` tries to simplify the many choices of :math:`R` by relying on Spearman's :math:`\rho` (pronounced *rho*), so don't worry too much about that for now.   

.. tip::

  As with anything in genomics, ``GUANinE``'s tasks can be split into two categories: Annotation and Perturbation.

Annotation Tasks
----------------
While not always considered 'exciting,' annotation tasks are the **core** performance measure of a successful model. If a model cannot *recognize* a gene, it's almost certainly not going to understand what happens when you try to *change* said gene. ::

  dnase_propensity
  
  ccre_propensity
  
  cons30
  
  cons100

Perturbation Tasks
------------------
These tasks don't necessarily 'build' on Annotation tasks, but it's fair to say they're the more difficult tasks -- and require far greater precision. The most infamous Perturbation tasks tend to be variant effect tasks, i.e. predicting what happens when a single nucleotide in a sequence is altered. ::

  gpra_c
  
  gpra_d
  
  clinvar_snv
  
  cadd_snv