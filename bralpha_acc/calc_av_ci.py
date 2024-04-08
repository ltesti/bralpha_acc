#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import numpy as np

def av_ci(fbra,efbra,fbrg,ebrg,rcii,ercii,abra_ak,eabra_ak):
    """
    Function to compute the Abra (and its error) starting from
    the measured fluxes (with errors), the ratio with error, and the 
    extinction ratio between bralpha and K, and its uncertainty
    """
    rag_obs = fbra/fbrg
