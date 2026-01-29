Sunburnt
========

Sunburnt is a Python-based interface for working with the `Apache Solr
<http://lucene.apache.org/solr/>`_ search engine.

It was written by Toby White <toby@timetric.com> for use in the `Timetric
platform <http://timetric.com>`_.

Please send queries/comments/suggestions to the `mailing list
<http://groups.google.com/group/python-sunburnt>`_.

Bugs can be filed on the `issue tracker <https://github.com/tow/sunburnt/issues>`_.

**Compatibility**: This version has been updated to support Python 3 and recent 
Solr releases (Solr 7, 8, 9+). It maintains backward compatibility with older 
Solr versions (1.3, 1.4, 3.1) and Python 2.7.

Full documentation can be found at http://opensource.timetric.com/sunburnt/index.html.

Dependencies
============

- Requirements:

  * Python 2.7 or Python 3.x
  * `httplib2 <http://code.google.com/p/httplib2/>`_ **or** `requests <http://requests.readthedocs.org/>`_
  * `lxml <http://lxml.de>`_

- Strongly recommended:

  * `pytz <http://pytz.sourceforge.net>`_

    Required for correct timezone handling with Python datetime objects.

  * `mx.DateTime <http://www.egenix.com/products/python/mxBase/mxDateTime/>`_

    Sunburnt will happily deal with dates stored either as Python datetime
    objects, or as mx.DateTime objects. The latter are preferable,
    having better semantics and a wider representation range. They will
    be used if present, otherwise sunburnt will fall back to Python
    datetime objects.

- Optional (only to run the tests)

  * `nose <http://somethingaboutorange.com/mrl/projects/nose/>`_

Recent Updates
==============

This version includes:

- **Python 3 support**: Full compatibility with Python 3.x while maintaining Python 2.7 support
- **Modern Solr field types**: Support for Point field types introduced in Solr 7+:
  
  * ``IntPointField``, ``LongPointField``, ``FloatPointField``, ``DoublePointField``
  * ``DatePointField``
  * Maintains backward compatibility with deprecated Trie and Sortable field types

- **API compatibility**: All existing APIs remain unchanged, ensuring backward compatibility
