# flake8: noqa

import sys

from qtpy import QT_VERSION

__appname__ = 'labeltoy'

__version__ = '0.0.1'
QT4 = QT_VERSION[0] == '4'
QT5 = QT_VERSION[0] == '5'
del QT_VERSION

PY2 = sys.version[0] == '2'
PY3 = sys.version[0] == '3'
del sys
