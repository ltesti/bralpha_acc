#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import numpy as np
#from astropy.tables import Table
import matplotlib.pyplot as plt


def plot_ratio(names, r, er, rm, erm, ax=None, filefig=None, maxrelerr=3., maxratio=3., myden="FBrg", mycol='red', myline="F$_{Br\alpha}$"):
    """
        This function plots the values of the ratios.
        
    """
    if not ax:
        fig, ax = plt.subplots(figsize=(18,6))
    
    nn = np.where(er>0.0)
    ax.axhline(y=np.mean(r[nn]), color=mycol, linestyle='--')
    ax.fill_between(names[nn], r[nn]*0.0+rm+erm, r[nn]*0.0+rm-erm, color=mycol, alpha=0.3)
    ngpfg = np.where((er/r <= maxrelerr) & (r <=maxratio) & (er>0.0))
    ax.errorbar(names[nn], r[nn], yerr = er[nn], fmt = 'o', alpha=0.2, color=mycol)
    ax.errorbar(names[ngpfg], r[ngpfg], yerr = er[ngpfg], fmt = 'o', color=mycol)
    #ax.set_xticks(rotation='vertical')
    ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(), rotation=70, ha='right')
    

    ax.set_xlabel('Class II objects')
    #ax.set_ylabel(r'{0} / F$_{Br\gamma}$'.format(myline))
    ax.set_ylabel(r'{0} / {1}'.format(myline, myden))
    if filefig:
        fig.savefig(filefig)
