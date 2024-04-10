#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import numpy as np


def lacc_fairlamb(lbrg,elbrgm,elbrgp):
    """
        This function returns the accretion luminosity from the Brgamma line luminosity, computed following Fairlamb et al. 2015
        
        params:
           'lbrg' : Log10(LBrg/Lsun)
           'elbrgm' : Log10((LBrg-eLBrg)/Lsun)
           'elbrgp' : Log10((LBrg+eLBrg)/Lsun) 
        returns:
           'lacc' : Log10(Lacc/Lsun) 
           'elaccm' : Log10((LBrg-eLBrg)/Lsun)
           'elaccp' : Log10((LBrg+eLBrg)/Lsun)
        """
    def lf15(ll):
        return ll*1.3+4.46
    lf =  lf15(lbrg)
    lfm = lf15(elbrgm)
    lfp = lf15(elbrgp)
    return lf, lfm, lfp