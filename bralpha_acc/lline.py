#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import numpy as np


def lline(f,ef,d_pc):
    """
        This function returns the accretion luminosity from the Brgamma line luminosity, computed following Fairlamb et al. 2015
        
        params:
           'f' : dereddened line flux 
           'ef' : error on  f
           'd_pc' : distance in parsec 
        returns:
           'lline' : Log10(Lacc/Lsun) 
           'llinem' : Log10((LBrg-eLBrg)/Lsun)
           'llinep' : Log10((LBrg+eLBrg)/Lsun)
           'delta_line' : average log error
        """
    #
    def pc_to_m(d):
        return 30856778570831268 * d
    lsun = (3.828 * (10 ** 26))
    Lline = -99.+np.zeros(len(f))
    Llinem = np.copy(Lline)
    Llinep = np.copy(Lline)
    delta_Lline = 0.0*np.copy(Lline)
    ng = np.where((f>0.0) & (ef<f))
    Lline[ng] = np.log10((f[ng] * 1.e-17 * 4 * np.pi * (pc_to_m(d_pc[ng]) ** 2)) / lsun)
    Llinem[ng] = np.log10(((f[ng]-ef[ng]) * 1.e-17 * 4 * np.pi * (pc_to_m(d_pc[ng]) ** 2)) / lsun)
    Llinep[ng] = np.log10(((f[ng]+ef[ng]) * 1.e-17 * 4 * np.pi * (pc_to_m(d_pc[ng]) ** 2)) / lsun)
    delta_Lline[ng] = ef[ng] / (f[ng] * np.log(10))
    
    return Lline, Llinem, Llinep, delta_Lline
 