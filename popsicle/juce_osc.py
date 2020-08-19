from functools import lru_cache as __lru_cache

import cppyy as __cppyy

from .utils import juce_bootstrap as __juce_bootstrap
from . import juce_events as __juce_events

__all__ = []

@__lru_cache(maxsize=1024)
def __juce_include():
    __cppyy.include("juce_osc/juce_osc.h")

__juce_bootstrap()
__juce_include()
