# -*- coding:UTF-8 -*-

import win32api
import win32print


def printer_loading(filename):
    open(filename, "r")
    win32api.ShellExecute(
        0,
        "print",
        filename,
        #
        # If this is None, the default printer will
        # be used anyway.
        #
        '/d:"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )

