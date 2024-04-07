
#!/usr/bin/env python
# coding=utf-8
from setuptools import setup

# read version number
exec(open("bralpha_acc/_version.py", "r").read())

# use README as long_description (for PyPI)
try:
    long_description = open("README.rst", "r", encoding="utf-8").read()
except TypeError:
    # under Python 2.7 the `encoding` keyword doesn't exist.
    print(
        "DEPRECATION: Python 2.7 has reached its end-of-life in 2020. "
        "Please upgrade your Python. SynthOptSpec is not meant for python 2 compatibility."
        "This software may not work as intended (or not work at all). "
    )
    long_description = open("README.rst", "r").read()


setup(
    name="bralpha_acc",
    version=__version__,
    packages=["bralpha_acc"],
    author="Leonardo Testi",
    author_email="ltesti120a@gmail.com",
    description="Utilities and scripts for the ECOGAL project to measure accretion in YSOs using the Bralpha/Brgamma lines.",
    long_description=long_description,
    install_requires=["numpy>=1.9", "matplotlib"],
    license="LGPLv3",
    url="https://github.com/ltesti/bralpha_acc",
    download_url="https://github.com/ltesti/bralpha_acc/archive/{}.tar.gz".format(
        __version__
    ),
    keywords=["science", "astronomy", "infrared spectroscopy","accretion disks"],
    classifiers=[
        "Development Status :: 0 - Under Development/Unstable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python :: 3",
    ],
)
