#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import numpy as np

#from .cardelli_alav import cardelli_alav
from .io import read_table
from .calc_cii_ratio import cii_ratio
from .plots_ratio import plot_ratio
from .line_flux_dered import fder
from .lline import lline
from .lacc_fairlamb import lacc_fairlamb

class cii_data(object):
    
    def __init__(self, filecsv, extinction="Cardelli", Rv=3.1):
        #
        # Read data
        self.data = read_table(filecsv)
        self.extinction = extinction
        self.Rv = Rv
        #
        # Extinction law definition
        if self.extinction=="Cardelli":
            awawl = None
        #
        # Deredden fluxes
        self.fbrgd, self.efbrgd, self.fpfgd, self.efpfgd, self.fbrad, self.efbrad= self.fefder()
        #
        # line ratios computation
        self.rbram, self.erbram, self.rbra, self.erbra = cii_ratio(self.fbrad,self.efbrad,self.fbrgd,self.efbrgd)
        self.rpfgm, self.erpfgm, self.rpfg, self.erpfg = cii_ratio(self.fpfgd,self.efpfgd,self.fbrgd,self.efbrgd)
        #
        # line luminosities
        self.lbrg, self.lbrgm, self.lbrgp, self.elbrg = lline(self.fbrgd,self.efbrgd,self.data['dist'])
        self.lbra, self.lbram, self.lbrap, self.elbra = lline(self.fbrad,self.efbrad,self.data['dist'])
        self.lpfg, self.lpfgm, self.lpfgp, self.elpfg = lline(self.fpfgd,self.efpfgd,self.data['dist'])  
        #
        # Accretion luminosities
        self.Lacc_Fairlamb, self.Lacc_Fm, self.Lacc_Fp = lacc_fairlamb(self.lbrg,self.lbrgm,self.lbrgp)
    
    #
    # Method to execute the ratio vs star plot
    def plot_ratio(self, plot="Bra"):
        #
        recognized = True
        if plot == 'Bra':
            #myline = "F$_{Br\alpha}$"
            myline = "FBra"
            mycol = "red"
            r = self.rbra
            er = self.erbra
            rm = self.rbram
            erm = self.erbram
        elif plot == 'Pfg':
            myline = "F$_{Pf\gamma}$"
            myline = "FPfg"
            mycol = "green"
            r = self.rpfg
            er = self.erpfg
            rm = self.rpfgm
            erm = self.erpfgm
        else:
            recognized=False
        if recognized:
            plot_ratio(self.data['Name'], r, er, rm, erm, filefig=None, maxrelerr=3., maxratio=3., mycol=mycol, myline=myline)
        else:
            print("Unrecognized plot ({0})".format(plot))
            
    #
    # Method to deredden the line fluxes 
    def fefder(self):
        #
        fbrad = fder(self.data['Fbra'], 4.05, self.data['Aj'], 1.25, awawl=None, Rv=self.Rv)
        efbrad = fder(self.data['eFbra'], 4.05, self.data['Aj'], 1.25, awawl=None, Rv=self.Rv)
        fbrgd = fder(self.data['Fbrg'], 2.166, self.data['Aj'], 1.25, awawl=None, Rv=self.Rv)
        efbrgd = fder(self.data['eFbrg'], 2.166, self.data['Aj'], 1.25, awawl=None, Rv=self.Rv)
        fpfgd = fder(self.data['Fpfg'], 3.74, self.data['Aj'], 1.25, awawl=None, Rv=self.Rv)
        efpfgd = fder(self.data['eFpfg'], 3.74, self.data['Aj'], 1.25, awawl=None, Rv=self.Rv)
        return fbrgd, efbrgd, fpfgd, efpfgd, fbrad, efbrad
         
        