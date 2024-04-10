#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import numpy as np

from .cardelli_alav import cardelli_alav

def fder(f, w, awl, wl, awawl=None, Rv=3.1, verbose=False):
    """
        This function returns the accretion luminosity from the Brgamma line luminosity, computed following Fairlamb et al. 2015
        
        params:
           'f' : Observed line flux
           'w' : wavelength of line
           'awl' : extinction in mag at reference wavelength
           'wl' : reference wavelength in um of extinction
           'awawl' : extinction ratio between w and wl (if None use Cardelli)
           'Rv' : value of the Rv parameter for the extinction law 
        returns:
           'fd' : dereddened line flux

        """
    #
    if not awawl:
        alav = cardelli_alav(np.array([wl,w]), Rv=Rv)
        awawl = alav[1]/alav[0]
    if verbose:
        print("Using extinction curve: A({0:5.3f})/A({1:5.3f})={2:5.3f}".format(w,wl,awawl))
    #
    aw = awawl*awl
    fact = np.exp(aw/1.086)
    #
    nb = np.where( f < 0.0 )
    fact[nb] = 1.0
    #
    return f*fact
