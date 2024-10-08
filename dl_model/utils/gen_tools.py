#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
#
# SCRIPT: used in main & process_plot scripts-.
# @AUTHOR: Fernando Diego Carazo (@buenaluna) -.
# start_date (Arg): juev 25 abr 2024 11:07:37 -03-.
# last_modify (Arg): mié 07 ago 2024 09:11:17 -03-.
#
# ======================================================================= INI79
# 1- include packages/modules/libraries/variables, etc.-.
from pathlib import Path
import yaml
# import os
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from numpy import linalg as LA
# print(dir()) # to see the names in the local namespace-.
# ======================================================================= END79

# ======================================================================= INI79
# 2- Classes, Functions, Methods, etc. definitions-.

# ======================================================================= INI79
# 2-1- remove columns with all values are equal to zero-.
def remove_cols_zeros(df):
    '''
    function remove_cols_zeros: remove columns whose values are Null/NaNs-.
    Variables:
    1- df: initial df-.
    2- Output:
    df: modified (or not) df-.
    n_cols_rem: number of columns removed-.
    '''
    
    n_cols_rem= 0  # by default = 0-.
    # find the zeros/Nulls/NaNs-.
    zeroes= (df==0.0) & (df.applymap(type)==float)
    # find columns with only zeroes-.
    cols= zeroes.all()[zeroes.all()].index.to_list()  # list with column indexes to be removed-.
    n_cols_rem= len(cols)  # numbers of columns to be removed-.
    # drop these columns-.
    df= df.drop(cols, axis=1) # remove columns with all values equal to zero-.

    return df, n_cols_rem
# ======================================================================= END79

# ======================================================================= INI79
# 2-2- print differences between two lists -.
def print_remove_cols(df_in, df_out):
    '''
    function print_remove_cols: print differences between two lists. In this case 
                                it is used to print the name of removed columns in
                                a pandasDF -.

    Variables:
    ==========
    df_in: list with a columns/features names of ORIGINAL pandasDF-.
    df_out: list with columns/features names of MODIFIED pandasDF-.

    Output:
    =======
    difference between two inputs (using set)-.
    '''
    print(set(list(df_out))- set(list(df_in)))
# ======================================================================= END79

# ======================================================================= INI79    
# 2-3- 2set the name of folder 2save figures-.
def folder_to_save_figs(ds_file_name: str, root_save_figs: str, r) -> str:
    '''
    function folder_to_save_figs: set the name of folders in which I 
                                  will save the figures-.

    Variables:
    ==========
    ds_file_name: name of the file to test-.
    root_save_figs: root folder to save figs (set in exec_env function)-.
    r (acronymous of 'root'): project root folder (set in exec_env function)-.

    Output:
    =======
    f_f (acronymous of 'figure_folders'): absolute PATH in which I will 
                                          save figures-.
    '''
    
    fold_name= str.split(ds_file_name, '.')[0]+'_figs'
    f_f= root_save_figs+ fold_name

    return f_f
# ======================================================================= END79

# - =======================================================================INI79
# 2-4- get the arguments from the config file-.
def get_args(path: Path):
    '''
    function get_args: get the arguments from the config file-.
    '''
    
    with open(path, 'r') as f: config= yaml.safe_load(f)
    return config
# - =======================================================================END79

# - =======================================================================INI79
# 2-5- to interpolate a straight line to a cloud of points-.
def adjust_line(x, y):
    ''' coefficients of interpolated stright line '''
    pearR= np.corrcoef(x.to_numpy(dtype=float), y)[1,0]
    A= np.vstack([x.to_numpy(dtype=float), np.ones(len(x))]).T
    m, c= np.linalg.lstsq(A,y)[0]
    return m, c, pearR
# - =======================================================================END79

# - =======================================================================INI79
# 2-6- calculate metrics between two pandas.DataFrame
def print_metrics(df1, df2)->int:
    '''general function to calculate emtrics between two datasets-.'''
    
    # print metrics-.
    print('Predicted case {0:>2}{1}{2:<6}{3:>2}{4:>10.6f}{5}'+
          '{6:<6}{7:>2}{8:>10.6f}{9}{10:<6}{11:>2}{12:>10.6f}{13}'.
          format(case,
                 '\n','MSE','=',np.round(mean_squared_error(y_pred, y_test), 6),
                 '\n','R2','=',np.round(r2_score(y_pred, y_test), 6),
                 '\n','RMSE','=',np.round(np.sqrt(mean_squared_error(y_pred, y_test)), 6),
                 '\n'
                 ))
    return 0
# - =======================================================================END79

# - =======================================================================INI79
# 2-7- convert seconds in hour:minutes:seconds-.                 
def convert_to_preferred_format(sec):
    sec= sec%(24*3600)  # seconds by day-.
    hour= sec// 3600  # hours by day-.
    sec%= 3600  # the rest of sec/3600 is the number of seconds-.
    min= sec// 60  # // cociente de una division en Python-.
    sec%= 60  # minutes-.
    # print('seconds in hours: {0}'.format(hour))
    # print('seconds in minutes: {0}'.format(min))
    return '{0:8.4f}hs. : {1:8.4f} min. : {2:8.4f} seg.'.format(hour, min, sec)
# - =======================================================================END79
