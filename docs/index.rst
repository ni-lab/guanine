.. guanine documentation overview file

================
GUANinE overview
================

``G``\ enome ``U``\ nderstanding ``A``\ nd a\ ``N``\ notation ``in`` silico ``E``\ valuation, or ``GUANinE``, is a benchmark for sequence-to-function models in genomics, concentrating on human (and eukaryotic) reference genomes. 


As a benchmark, ``GUANinE`` offers modelers a chance to evaluate and develop competitive models on controlled, high-quality data designed for generalizability. Unique to ``GUANinE`` is its unparalleled scale (~ 1M ``test`` set datapoints, not including the ``train`` or ``dev`` splits), which allows for deeper profiling of experimental models and more thorough statistical testing.    


Check out the `getting started`_ page for tips on downloading and accessing the data, or inspect the `current leaderboard`_. 


GUANinE Tasks, at a high level
------------------------------

+---------------+---------------------+-------------------+-------------------+
| task name     |      task type      | task target       |  domain           |
+===============+=====================+===================+===================+
| `dnase_prop`_ |    Accessibility    | Sequence region   | Human (hg38)      |
+---------------+---------------------+-------------------+-------------------+
| `ccre_prop`_  | Functional elements | Sequence region   | Human (hg38)      |
+---------------+---------------------+-------------------+-------------------+
| `cons30`_     | Seq. Conservation   | Sequence region   | Human-Mammal      |
+---------------+---------------------+-------------------+-------------------+
| `cons100`_    | Seq. Conservation   | Sequence region   | Human-Vertebrate  |
+---------------+---------------------+-------------------+-------------------+
| `gpra-c`_     | Promoter expression | Short  sequence   | Yeast (synthetic) |
+---------------+---------------------+-------------------+-------------------+
| `gpra-d`_     | Promoter expression | Short sequence    | Yeast (synthetic) |
+---------------+---------------------+-------------------+-------------------+
| `cadd-snv`_   | Deleteriousness     | Sequence variant  | Human (simulated) |
+---------------+---------------------+-------------------+-------------------+
| `cadd-indel`_ | Deleteriousness     | Indel variant     | Human (simulated) |
+---------------+---------------------+-------------------+-------------------+
| `clinvar-snv`_| Pathogenicity       | Sequence variant  | Human (clinical)  |
+---------------+---------------------+-------------------+-------------------+

.. seealso:: For a detailed comparison of tasks, consult the `task comparison`_ page. 

|

``GUANinE`` is developed and maintained by `eyes robson`_, a PhD candidate under `Nilah Ioannidis`_. To cite ``GUANinE``, use the following .bibtex

.. code-block:: 
    :caption: v1.0 .bibtex
    
    @InProceedings{pmlr-v240-robson24a,
    title = 	 {GUANinE v1.0: Benchmark Datasets for Genomic AI Sequence-to-Function Models},
    author =       {robson, eyes s. and Ioannidis, Nilah},
    booktitle = 	 {Proceedings of the 18th Machine Learning in Computational Biology meeting},
    pages = 	 {250--266},
    year = 	 {2024},
    editor = 	 {Knowles, David A. and Mostafavi, Sara},
    volume = 	 {240},
    series = 	 {Proceedings of Machine Learning Research},
    month = 	 {30 Nov--01 Dec},
    publisher =    {PMLR},
    pdf = 	 {https://proceedings.mlr.press/v240/robson24a/robson24a.pdf},
    url = 	 {https://proceedings.mlr.press/v240/robson24a.html}
    }


.. _`task comparison`: ./task_comparison.html
.. _`dnase_prop`: ./tasks/dnase_propensity.html
.. _`ccre_prop`: ./tasks/ccre_propensity.html
.. _`cons30`: ./tasks/cons30.html
.. _`cons100`: ./tasks/cons100.html
.. _`gpra-c`: ./tasks/gpra_c.html
.. _`gpra-d`: ./tasks/gpra_d.html
.. _`cadd-snv`: ./tasks/cadd_snv.html
.. _`cadd-indel`: ./tasks/cadd_indel.html
.. _`clinvar-snv`: ./tasks/clinvar_snv.html

.. _`getting started`: ./installation.html
.. _`current leaderboard`: ./leaderboard.html
.. _`eyes robson`: https://eyes-robson.github.io
.. _`Nilah Ioannidis`: https://vcresearch.berkeley.edu/faculty/nilah-ioannidis
