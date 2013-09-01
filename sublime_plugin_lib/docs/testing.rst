.. include:: vars.rst

***************
Testing plugins
***************

`Sublime Text` provides an API via modules ``sublime`` and ``sublime_plugin``,
which normally won't be available during testing. In order to allow for
testing most parts of a plugin, |lib_name_quoted| provides a cut down
version of these two modules (with of course limited functionality). Use in
your tests with::

.. code-block:: python

    import sys
    from sublime_plugin_lib.mock import sublime, sublime_plugin
    sys.modules['sublime'] = sublime
    sys.modules['sublime_plugin'] = sublime_plugin

.. toctree::
    :maxdepth: 2

.. _module_mock_sublime:

:mod:`sublime` Module
=====================

.. automodule:: sublime_plugin_lib.mock.sublime
    :members:
    :undoc-members:
    :show-inheritance:

.. _module_mock_sublime_plugin:

:mod:`sublime_plugin` Module
============================

.. automodule:: sublime_plugin_lib.mock.sublime_plugin
    :members:
    :undoc-members:
    :show-inheritance:
