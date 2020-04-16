# -*- coding: utf-8 -*-
import sys
import os


if os.getcwd() not in sys.path:
    sys.path.insert(0, os.getcwd())


from .core import LazySettings, settings  # noqa
