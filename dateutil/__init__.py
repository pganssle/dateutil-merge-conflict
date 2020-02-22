# -*- coding: utf-8 -*-
import sys
import importlib

try:
    from ._version import version as __version__
except ImportError:
    __version__ = 'unknown'

__all__ = ['easter', 'parser', 'relativedelta', 'rrule', 'tz',
           'utils', 'zoneinfo']


MIN_LAZY_LOAD_PY_VERSION = (3, 7, 0)
if sys.version_info >= MIN_LAZY_LOAD_PY_VERSION:
	def __getattr__(name):
		if name in __all__:
			return importlib.import_module('.' + name, __name__)
		raise AttributeError("module {!r} has not attribute {!r}".format(__name__, name))
