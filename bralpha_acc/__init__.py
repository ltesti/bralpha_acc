from ._version import __version__

import matplotlib

# To avoid Runtime Error
# RuntimeError: Python is not installed as a framework. The Mac OS X backend
# will not be able to function correctly if Python is not installed as a framework.
# See the Python documentation for more information on installing Python as a
# framework on Mac OS X. Please either reinstall Python as a framework, or try
# one of the other backends.
# If you are using (Ana)Conda please install python.app and replace the use of
# 'python' with 'pythonw'.
# See 'Working with Matplotlib on OSX' in the Matplotlib FAQ for more information.
# https://matplotlib.org/faq/osx_framework.html

if matplotlib.get_backend().lower() == 'macosx':
    matplotlib.use('TkAgg')

from .class_ii import cii_data
from .io import read_table
from .cardelli_alav import cardelli_alav
from .calc_cii_ratio import cii_ratio
from .line_flux_dered import fder
#from .plots_ratio import plot_ratio
from .lacc_fairlamb import lacc_fairlamb


