
.. admonition:: Under development
    
    The cadd-indel datasets are still being refined, and information on this page is liable to change.    

======================
cadd-indel
======================

 | tags: deleteriousness, variant interpretation, insertions, deletions, indels, CADD,

tl;dr
------ 
``cadd-indel`` is a insertion-deletion (indel) modeling task, where models attempt to separate a set of 'benign' variants from a set of 'deleterious' (simulated) variants, as in the `original CADD`_\ .   

overview
--------

Aligning a personal (i.e. real) genome to the a reference genome creates a variant call file --  a list of all divergences from the reference sequence. These divergences can often be **atomized** into variants, as many (not all) regions of the genome are additive (i.e. non-epistatic). Indel variants, being intermediate in size (short deletions or multi-bp **insertions**), are more complex than single-nucleotide substitutions, but are still frequent and easier to model than large-scale structural variants. 

The `original CADD`_ model demonstrated that deleterious (or 'evolutionarily harmful') variants can be modeled *in simulation* by contrasting:
    - proxy benign variants: alleles derived from the human-chimp common ancestor, versus
    - proxy deleterious variants: simulated random mutations

This allows for the construction of an ancestrally-biased deleteriousness estimator -- one independent of large-scale population databases like `gnomAD`_\ . While such datasets can provide invaluable information about variant frequency (frequent variants are almost cetainly not deleterious), they themselves are often biased due to volunteerism and historical biases in medicicine.

build details
-------------

[Under development] 


appears in
---------------- 
`GUANinE v1.1`_

original citations
------------------

Kircher M, Witten DM, Jain P, O'Roak BJ, Cooper GM, Shendure J.
A general framework for estimating the relative pathogenicity of human genetic variants.
Nat Genet. 2014 Feb 2. doi: 10.1038/ng.2892.
PubMed PMID: 24487276.

Rentzsch P, Witten D, Cooper GM, Shendure J, Kircher M.
CADD: predicting the deleteriousness of variants throughout the human genome.
Nucleic Acids Res. 2018 Oct 29. doi: 10.1093/nar/gky1016.
PubMed PMID: 30371827.

Schubach M, Maass T, Nazaretyan L, Röner S, Kircher M.
CADD v1.7: Using protein language models, regulatory CNNs and other nucleotide-level scores to improve genome-wide variant predictions.
Nucleic Acids Res. 2024 Jan 5. doi: 10.1093/nar/gkad989.
PubMed PMID: 38183205.


.. _`GUANinE v1.1`: https://github.com/ni-lab/guanine/404
.. _`original CADD`: https://www.doi.org/10.1038/ng.2892
.. _`gnomAD`: https://gnomad.broadinstitute.org/ 