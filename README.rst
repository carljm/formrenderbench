To run form-rendering benchmarks:

1. Install `djangobench`_ in a virtualenv according to `the instructions`_.

2. Don't make svn clones of Django as shown there, just clone
   git://github.com/carljm/django.git and make sure you have local clones of
   the "master" and "soc2011/form-rendering" branches.

3. Install this project in the same virtualenv (``pip install -e .`` should
   do it if you have it cloned locally).

4. From the root of your Django git clone, with your virtualenv active, run
   something like ``djangobench --vcs=git --control=master --experiment=soc2011/form-rendering --trials=1000 --benchmark-dir /path/to/here/formrenderbench/benchmarks``

.. _djangobench: https://github.com/jacobian/djangobench
.. _the instructions: https://github.com/jacobian/djangobench/blob/master/README.rst


