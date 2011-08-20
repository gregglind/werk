==================================
werk - simple project tracking
==================================

install
--------

``pip install -e git+git://github.com/gregglind/werk#egg=werk``  

use
----

::

    werk start proj1
    werk msg proj1  "researched how fabric works"  # note the unix style quoting
    werk stop proj1
    werk status proj1 

gritty details
---------------

``werk`` just writes lines to ``~/.werklog``.  Edit that as you see fit.


develop / contribute
-----------------------

* fork and clone:  ``git@github.com:gregglind/werk.git``
* ``cd werk``
* ``pip install -e .`` # to install your dev version.  


