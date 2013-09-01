# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import sublime
import sublime_plugin
import webbrowser

class SublimePluginLibOpenUrlInDefaultBrowserCommand(sublime_plugin.ApplicationCommand):

    """
    Sublime Text application command
    ``sublime_plugin_lib_open_url_in_default_browser``.

    Opens given URL in a new browser tab.
    """

    def run(self, **kwargs):
        if "url" not in kwargs:
            return

        webbrowser.open_new_tab(kwargs["url"])


def open_url_in_default_browser(url):
    """
    Wrapper for Sublime Text command
    ``sublime_plugin_lib_open_url_in_default_browser``.
    """

    sublime.run_command(
        "sublime_plugin_lib_open_url_in_default_browser", {"url": url})
