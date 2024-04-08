#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import numpy as np
#from astropy.tables import Table
import pandas as pd


def read_table(filename,preset='ClassII',columns=None):
    """
        This function reads a table with data in the format written by the 
        extended scripts from Samuele Gozzi Colab.
        
        params:
           'filename' : full path to the input file
        returns:
           'mydic' : dictionary containing the data that has been read 
        """
    # Step zero: decide the columns of interest
    column_presets = {
        'ClassII' : ["Name","dist","Lstar","Aj","Fbrg","eFbrg","Fbra","eFbra","L_acc_Fairlamb"],
        'ClassI' : ["Name","Lbol","Tbol","dist","Fbrg","eFbrg","Fbra","eFbra","Av","eAv","Abrg","eAbrg","Abra","eAbra","Lacc","eLacc","TbH24","iH24"],
        }
    if not columns:
        if preset:
            if preset in column_presets.keys():
                mycols = column_presets[preset]
        else:
            print("Warning: cannot work properly with preset={0} and columns=None\n".format(preset))
            print("         recognized presets are: {0}\n".format(column_presets.keys()))                 
            print("         we continue using:\n")
            print("         preset = 'ClassII'\n")
            print("            PLEASE CHECK THIS IS WHAT YOU NEED\n")
    else:
        mycols = columns
    
    # Step one: read the data in astropy table format
    #t = Table.read(filename,format='ascii')
    t = pd.read_csv(filename)
    
    # Step two: fill in the dictionary converting the table columns into arrays
    mydic = {}
    for col in mycols:
        mydic[col] = np.array(t[col])
    
    # Return data
    return mydic 