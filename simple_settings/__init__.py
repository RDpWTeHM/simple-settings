# -*- coding: utf-8 -*-
import sys
import os
from .core import LazySettings, settings  # noqa


if os.getcwd() not in sys.path:
    sys.path.insert(0, os.getcwd)
