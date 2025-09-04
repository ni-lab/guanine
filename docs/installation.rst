================================
Installing the GUANinE Benchmark 
================================

tl;dr
-----

GUANinE datasets are built on ``Git`` and ``Git LFS``; optional (recommended) packages are ``twobitreader``, ``scipy``, ``pandas``, and ``transformers``  -- but feel free to use your own tool to parse sequences, tally results, read files, and load models (respectively).

example installation
--------------------

1. Most systems (Colab, HPC, etc) come pre-packaged with ``Git``, but you should consult `Git's documentation`_ if ``which git`` returns nothing in your console.


2. Next, to install ``Git LFS``, you should try: ::

    git lfs install

  If this returns an error, it means your system can't find the proper installation files (rip). Those using conda/mamba can try ``conda install git-lfs``. Alternatively, for mac you can try ``brew install git-lfs``, while for linux check the guide `here`_. 


3. Finally, to install the optional i/o tools with ``pip``: ::

    pip install twobitreader scipy pandas 
    pip install transformers 

.. _`here`: https://github.com/git-lfs/git-lfs/blob/main/INSTALLING.md
.. _`Git's documentation`: https://git-scm.com/downloads/