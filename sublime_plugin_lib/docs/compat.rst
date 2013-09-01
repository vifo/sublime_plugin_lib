.. include:: vars.rst
.. module:: sublime_plugin_lib.compat
   :synopsis: Compatibility layer for Python 2 and 3
.. moduleauthor:: Victor Foitzik <vifo@cpan.org>

*******************
Compatibility layer
*******************

`Sublime Text 2` uses Python 2.6 under the hood, while `Sublime Text 3`
switched to Python 3. In order to smooth out the rough edges and allow plugins
to run unaltered under ST2 and ST3, |lib_name_quoted| provides a thin
compatibility layer similar to, but lighter than six_.

.. _six: https://pypi.python.org/pypi/six/

.. code-block:: python

    import sublime_plugin_lib.compat

Globals
=======

.. data:: PY2

Boolean, ``True``, if running under Python 2, ``False`` otherwise.

.. data:: PY3

Boolean, ``True``, if running under Python 3, ``False`` otherwise.

Types
=====

This module also provides aliases for different types used in Python 2 and
Python 3.

.. code-block:: python

    import sublime_plugin_lib.compat

    spam = 'egg'
    if isinstance(spam, compat.string_type):
        pass

Typical use of these aliases is for :func:`py3:isinstance` or
:func:`py3:issubclass` checks.

.. data:: binary_type

   List of possible integer data types. Contains :func:`py2:int` and
   :func:`py2:long` in Python 2 and :func:`int` in Python 3.

.. data:: integer_types

   List of possible integer data types. Contains :func:`py2:int` and
   :func:`py2:long` in Python 2 and :func:`int` in Python 3.

.. data:: string_types

   List of possible text data types. This is :func:`py2:basestring` in Python
   2 and :class:`str() <py3:str>` in Python 3.

.. data:: text_type

   Type for representing Unicode text data. This is :func:`py2:unicode` in
   Python 2 and :class:`str() <py3:str>` in Python 3.

Exceptions
==========

.. exception:: WindowsError

   Normally, the ``WindowsError`` exception is only available under Windows.
   Trying to catch this exception on non-Windows will result in errors. To get
   around this, import ``WindowsError`` from this module. It will provide a
   dummy ``WindowsError`` exception on non-Windows platforms::

    .. code-block:: python

    from sublime_plugin_lib.compat import WindowsError
    try:
        ...
    catch (WindowsError) as e:
        pass

References
==========

`http://www.voidspace.org.uk/python/articles/porting-mock-to-python-3.shtml`_
