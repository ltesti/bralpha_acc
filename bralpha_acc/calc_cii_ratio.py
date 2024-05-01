#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import numpy as np

#from .cardelli_alav import cardelli_alav
from .line_flux_dered import fder

def cii_ratio(f1,ef1,f2,ef2):
    """
    Function to compute the Abra (and its error) starting from
    the measured fluxes (with errors), the ratio with error, and the 
    extinction ratio between bralpha and K, and its uncertainty
    """
    ng = np.where((np.isfinite(f1)) & (np.isfinite(f2)) & (ef1>0.0) & (ef2>0.0))
    #
    r = (f1/f2)
    er = r * 0.0
    er[ng] = r[ng] * np.sqrt((ef1[ng] / f1[ng]) ** 2 + (ef2[ng] / f2[ng]) ** 2)
    #
    r_mean = np.mean(r[ng])
    er_mean = np.sqrt( ((np.mean(r[ng])-r[ng])**2).sum() / len(r[ng]) ) / np.sqrt(len(r[ng]))
    #
    return r_mean, er_mean, r, er
