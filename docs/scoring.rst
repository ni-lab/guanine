=====================
How Models are Scored
=====================

 | tags: model evaluation, evaluating models, test set, spearman rho, results

tl;dr
------ 

``GUANinE`` uses Spearman's :math:`\rho` (pronounced 'rho') to score model predictions. We suggest ``stats.spearmanr`` from the ``scipy`` package if you don't have a better implementation.

.. important::
    Implementations of :math:`\rho` may handle ties differently. We recommend adding `'jitter'`_ to your predictions to test for sensitivity to minute perturbation. See below for how-to. 

scoring overview
----------------
Speaman's :math:`\rho` is a robustified variant of Pearson's correlation coefficient. Unlike Pearson's R, it is immune to affine (``y = mx + b``) transformations, so there is no need to worry about a 'cutoff' score or whether you power/log/Box-Cox transformed your predictions. Do note that it still presumes *increasing* results -- predictions that are identical will impede its measurement.

By construction, most test set in ``GUANinE`` have private labels, just like in `other AI benchmarks`_ and `Kaggle`_ contests. This prevents 'accidental' cheating by design, and it also helps to extend the life of the benchmark. 

To get your test set results, see the `submission`_ page [automatic scoring is not yet live].

example usage
-------------

with a ``GUANinE`` task dataset in ``dev_dat``, try the following:

.. code-block:: 
    :caption: using scipy's stats.spearmanr

    from scipy.stats import spearmanr

    y_dev = dev_dat['y'] 
    preds = my_model.predict(dev_dat['tokenized_sequences']) # replace with your own function

    ## compute the results & its two-tailed significance (i.e. chance of being non-zero)
    spear, spear_signif = spearmanr(preds, y_dev)

    ## if you want to pretty print, use numpy.round
    print(np.round(spear*100., 4)) ## e.g. 74.XXYY

.. note:: 
    To submit your test set predictions for scoring, you will need to include your development set results, so keep these handy when submitting predictions.  

preventing 'hiccups'
--------------------

If your model is a classifier then measurements may be more accurate with a continuous relaxation, e.g. ``model.predict_proba`` for ``scikit-learn`` modules. This prevents ``spearmanr`` from having to resolve ties, but you can also use jitter:

.. code-block::
    :caption: sensitivity analysis with jitter

    preds = my_model.predict(dev_dat['tokenized_sequences']) ## replace with your own function

    epsilon = 0.01 # make this small, relative to your predictions
    for i in range(5):
        jitter = np.random.randn(preds.shape[0]) * epsilon
        spear = spearmanr(preds + jitter, y_dev)[0]
        print(spear)

If the code above produces *very* disparate results, e.g. a spearman score of 0.84 --> 0.76, then you should probably not report the un-jittered score (as it's an artifact of ``spearmanr``'s tie-handling -- this happens with VEP, whose scores we always jitter). We recommend running 30-50 'jitters' and reporting the average result to accurately reflect your model's performance.

Finally, your model may have a few not-a-numbers entries (``NaN``\ s), especially if combining many intermediate predictors. We've found replacing ``NaN``\ s with the mean value improves performance the most, but you are welcome to experiment with this on the **development set** before submitting your final predictions. 

.. code-block::
    :caption: replacing NaNs in predictions

    preds = pd.Series(preds) # easiest way to fill a vector

    ## .mean() skips NaNs by default
    preds.fillna(preds.mean()) # you can replace preds.mean() with 0., etc

    spear, spear_signif = spearmanr(preds, y_dev) # compute your imputed score


A small number of ties (e.g. ~ 1% of the dataset) will not materially impact your ``spearmanr`` score, so don't worry too much about needing to impute then jitter your results. 

.. _`submission`: ./submission.html
.. _`other AI Benchmarks`: https://super.gluebenchmark.com/
.. _`'jitter'`: https://en.wikipedia.org/wiki/Jitter
.. _`Kaggle`: https://www.kaggle.com/ 