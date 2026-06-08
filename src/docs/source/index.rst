.. _home:

Get Started with Shapley Value Regression
=========================================
To get started, you can use the `ShapleyValue` class from the package. Here's a quick 
example using a built-in dataset:

- :ref:`Installation Instructions <installation>`
- :ref:`Quick Start Guide <quickstart>`

Historical Background
=====================

Shapley Value Regression is rooted in cooperative game theory, introduced by 
`Lloyd Shapley <https://en.wikipedia.org/wiki/Lloyd_Shapley>`_ in 1953. It addresses 
a fairness question: when outcomes are created jointly, how should credit be shared? 
The Shapley value answers this by averaging each participant's contribution 
across all possible coalitions.

:ref:`Historical Background <historical-background>`

Why Shapley Value Regression?
=============================

Shapley Value Regression provides an alternative perspective by allocating model
explanatory power among predictors using principles from cooperative game
theory. It is especially useful when predictors are correlated and share information, 
as traditional methods can be misleading in such cases.

:ref:`Why Shapley Value Regression? <shapley-value-regression>`

The Shapley Value Approach
==========================

Shapley Value Regression treats each predictor as a participant in a
cooperative game. The total explanatory power of the model is the reward that
must be distributed among all predictors.

:ref:`The Shapley Value Approach <mathematical-foundation>`

Comparison with Alternative Methods
===================================

Shapley Value Regression is often preferred when understanding variable
contribution is more important than computational efficiency. It provides a fair 
allocation of explanatory power, especially when predictors are correlated and share information.

:ref:`Comparison with Alternative Methods <comparison-with-alternative-methods>`

Summary
=======
 
Shapley Value Regression does not replace traditional regression analysis. 
Instead, it provides an additional perspective on how explanatory power should 
be attributed among predictors.
 
While the method is computationally more expensive than coefficient-based approaches, 
it offers a principled and theoretically grounded solution to one of the most challenging 
problems in regression analysis:
 
**How should explanatory power be fairly distributed when predictors share information?**
 
For models with a manageable number of predictors, Shapley Value Regression can provide 
insights that are often difficult to obtain using traditional importance measures alone.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :hidden:

   module/installation
   module/quickstart
   module/class-ref
   historical-background
   shapley-value-regression
   mathematical-foundation
   comparison-with-alternative-methods
   computational-considerations