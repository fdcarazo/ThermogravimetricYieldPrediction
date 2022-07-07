#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
#
#
# procesamiento de los datos (analisis, depuracion y curacion)
# de un biodigestor provisto por la
# Dra.- Ing. Rosa Rodriguez - IIQ - CONICET - FI - UNSJ-.
#
# start_date: mar jul  5 13:11:15 -03 2022 -.
# last_modify: 


# importamos modulos-.
import pandas as pd
import glob
import os
from aux_proc import check_reg_exp
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.express as px
import numpy as np
# from scipy import interpolate

# Configuracion warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')

root_path = '/home/fcarazo/diploDatos2022/trabajoPirolisis_IIQ/'

# 1- =================================================================
# load files and built PandasDataFrames-.
# load files-.
files_list = list()  # empty list-.
files_list = glob.glob(os.path.join(str(root_path), '*.csv'),
                       recursive='True')  # strObject-.
print('{0}Se encontraron {1} archivos *.csv. Sus nombres son:{2}'.
      format('\n', len(files_list), '\n'))
[print(i) for i in files_list]  # compresion list-.

reg_exp = 'marcstalk'  # string leave out in search-.

# Built PandasDataFrames-.
pd_list_name = list()  # list with PandasDataFrames names-.
i = 0
for files_names in files_list:
    if check_reg_exp(reg_exp, files_names):  # don't load unlabeled data-.
        pass
    else:
        # print(check_reg_exp(reg_exp, files_names))
        # print(files_names)
        i = i+1
        df_name = 'df_{0}'.format(i)
        # index_col= None or index_col=False don't work-. why?-.
        exec('df_' + str(i) + "= pd.read_csv(files_names, index_col=0)")
        # modify label columnas-.
        pd_list_name.append(df_name)

        print(pd_list_name)

# chequeo los dataframes-.
[print(eval(i_pd_name)) for idx, i_pd_name in enumerate(pd_list_name)]

# - ===================================================================

# - ===================================================================
ndatas = 3  # numbers of rows to show with sample method-.
nl = '\n'  # newline character. Will be used with f-'s prints statements-.

DS_name = 'Prediccion del rendimiento de un proceso de Pirolisis ' + \
    'con escobajo. DataFrame provisto por el IIQ-UNSJ-CONICET'

# actividades de esta primer entrega-.
print(f' Exploracion, visualizacion, analisis y curacion '+
      f'del DS{nl}{DS_name}{nl}')


# - ===================================================================
# INI @ ANALISIS_1 ----
# ''' @FDC-comment muestreo en el orden preestablecido de los 3 (tres)
# registros-.
print('{0}{1}Visualizacion en el ORDEN DEL DataSet (DS){2}'.
      format('\n', '\t /// << --- >> /// ', '\n'))
[print('{0}Visualizamos {1} registros del DS {2}{3}'.
       format('\n', ndatas+1, '\n', eval(pd_list_name[i])[:ndatas]))
 for i in np.arange(len(pd_list_name))]


# ''' @FDC-comment muestreo aleatorio de 3 (tres) registros-.
print('{0}{1}Visualizacion ALEATORIA DEL DataSet (DS){2}'.
      format('\n', '\t /// << --- >> /// ', '\n'))
[print('{0}Visualizacion ALEATORIA de {1} registros del DS {2}{3}'.
       format('\n', ndatas+1, '\n', eval(pd_list_name[i])[:ndatas]))
 for i in np.arange(len(pd_list_name))]

# @ ANALISIS_1: -.
# FIN @ ANALISIS_1 ----
# - ===================================================================


