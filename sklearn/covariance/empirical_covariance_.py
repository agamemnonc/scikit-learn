
# THIS FILE WAS AUTOMATICALLY GENERATED BY deprecated_modules.py
import sys
from . import _empirical_covariance
from ..externals._pep562 import Pep562
from ..utils.deprecation import _raise_dep_warning_if_not_pytest

deprecated_path = 'sklearn.covariance.empirical_covariance_'
correct_import_path = 'sklearn.covariance'

_raise_dep_warning_if_not_pytest(deprecated_path, correct_import_path)

def __getattr__(name):
    return getattr(_empirical_covariance, name)

if not sys.version_info >= (3, 7):
    Pep562(__name__)
