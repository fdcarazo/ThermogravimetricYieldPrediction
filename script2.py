#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
#
#
# script para armar los archivos csv para procesar los datos
# Prof. Dra.- Ing. Rosa Rodriguez - IIQ - CONICET - FI - UNSJ-.
#
# start_date: lun 04 jul 2022 09:50:29 -03-.
# last_modify: mie 06 jul 2022 23:44:05 -03-.


# importamos modulos-.
import pandas as pd
import subprocess as sp
# Configuracion warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')

# clean terminal-.
sp.run(['clear'])

# directorio y archivo con los datos-.
root_path = '/home/fcarazo/diploDatos2022/trabajoPirolisis_IIQ/'
fileName = 'DatosParaRNA_Orig.xlsx'


# 1- antes de comenzar chequeo que exista el directorio y el archivo-.
# PENDIENTE-.

# header[0,1]  ==> lista con posiciones de filas que se combinaran en
#                  un indice multiple.
vel_enfr = ['5 Kmin', '10 Kmin', '15 Kmin']  # velDeEnfr-.
df_names = list()
df_list = list()
for i, i_vel_enfr in enumerate(vel_enfr):
    # print(i_vel_enfr, i)
    df_name = ''.join(['df', i_vel_enfr.replace(' ', '')])
    df_names.append(df_name)
    df = pd.read_excel(root_path + fileName, header=[0, 1],
                       sheet_name=i_vel_enfr
                       )
    # borramos la primer fila MultiIndex: "Saltk" y "Marc"-.
    df = df.droplevel(level=0, axis=1)
    # borramos la segunda columna "Index" (indices de Excel)-.
    # df = df.drop(['index'], axis=1) # it doesn't work-.
    # df = df.reset_index(drop=True, inplace=True)

    if i_vel_enfr.replace(' ', '') == '5Kmin':
        df.loc[:, 'vel_cal'] = 5
    elif i_vel_enfr.replace(' ', '') == '10Kmin':
        df.loc[:, 'vel_cal'] = 10
    elif i_vel_enfr.replace(' ', '') == '15Kmin':
        df.loc[:, 'vel_cal'] = 15

    df_list.append(df)

    print('Contenido del DataFrame {0}{1}'.format('\n', df_name))
    # dfName.index.name = ''.join(['df', iVelEnfr.replace(' ', '')])
    print('Nombre del DataFrame {0}{1}'.format(df_list[i].index.name, '\n'))


# eliminamos la fila 0 -cero, i.e. primera- con las unidades de cada
# PandasDataFrame-.
df_list = list(map(lambda x: x.drop(labels=0, axis=0).reset_index(), df_list))
# eliminamos la columna 'index' -indice de excel- en cada PandsDataFrame-.
df_list = list(map(lambda x: x.drop(['index'], axis=1), df_list))

print(df_list)
print('{0}{1}'.format('\n', len(df_list)))
print([print(df_list[i].columns) for i in range(len(df_list))])


# built lists DataSet-.
def built_dataset(df_l: list):
    dfs_stalk = list()
    dfs_marc = list()
    for idx, i_df_name in enumerate(df_l):
        dfs_stalk.append(i_df_name.iloc[0:, [0, 1, 2, 6]])
        dfs_marc.append(i_df_name.iloc[0:, [3, 4, 5, 6]])
        # print(idx, type(i_df_name))
    return dfs_stalk, dfs_marc


df_stalk_alls, df_marc_alls = built_dataset(df_list)


'''
print(len(df_stalk_alls))
[print(df_stalk_alls[i].shape) for i in range(len(df_stalk_alls))]
[print(type(df_stalk_alls[i])) for i in range(len(df_stalk_alls))]
[print(df_stalk_alls[i]) for i in range(len(df_stalk_alls))]

print(len(df_marc_alls))
[print(df_marc_alls[i].shape) for i in range(len(df_marc_alls))]
[print(type(df_marc_alls[i])) for i in range(len(df_marc_alls))]
[print(df_marc_alls[i]) for i in range(len(df_marc_alls))]
'''

# concatenamos (por filas) los DFs-.
df_stalk = pd.concat(df_stalk_alls, axis=0, ignore_index=True)
df_marc = pd.concat(df_marc_alls, axis=0, ignore_index=True)

# shufleamos y re-escribimos los indices-.
# check sklearn.utils.shuffle() and np.random.shuffle().
df_stalk = df_stalk.sample(frac=1).reset_index(drop=True)
df_marc = df_marc.sample(frac=1).reset_index(drop=True)

print(df_stalk)
print(df_marc)

# save DataSets in csv format-.
df_stalk.to_csv(root_path+'stalk.csv')
df_marc.to_csv(root_path+'marc.csv')
