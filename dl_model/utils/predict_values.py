#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
##
# class to predict values-.
# @AUTHOR: Fernando Diego Carazo (@buenaluna) -.
#
# start_date (Fr): Wed Mar 20 15:46:09 CET 2024-.
# last_modify (Fr): -.
# last_modify (Arg): mié 07 ago 2024 21:42:56 -03-.
##
# ======================================================================= INI79

# print(dir()); input(1)

# import packages/libraries/modules-.
import pandas as pd

import numpy as np
import torch


class Predict_NN():
    def __init__(self, df, feat_names, targ_names, feat_scal,
                 targ_scal, model):
        self.df = df
        self.feat_names = feat_names
        self.targ_names = targ_names
        self.feat_scal = feat_scal
        self.targ_scal = targ_scal
        self.model = model
        
    def plot_predict(self, var, x, n_points, n_nn):
        '''
        function to predict
        var: variable to var-.
        x: range of "var" variables values-.
        n_points: len(x)-.
        n_nn: number of NN to calculate uncertanity-.
        '''
        
        df_proof = pd.DataFrame(data=x, columns=[str(var)])
        
        row_to_copy = pd.DataFrame(self.df.loc[np.random.randint(1,
                                                                 self.df.shape[0])])
        print(row_to_copy, type(row_to_copy),
              row_to_copy.loc['nu32',:].values, sep='\n'); input(44)
        print(row_to_copy,type(row_to_copy),row_to_copy.loc['nu32',:].values,sep='\n'); input(44)

        for icol,col in enumerate(self.df[self.feat_names+self.targ_names].columns.to_list()):
            if col!=var:
                ## val_to_add=np.random.uniform(self.df[[str(col)]].min(),self.df[[str(col)]].max())
                val_to_add=row_to_copy.loc[col,:].values
                df_proof[str(col)]=np.full((len(x),1),val_to_add)
        print(df_proof);input(55)

        ## syntetic df to Numpy-.
        df_proof_feat_np=df_proof[self.feat_names].to_numpy(dtype=float)
        df_proof_nuF_np=df_proof[var].to_numpy(dtype=float)

        ## print(df_proof,df_proof.columns,sep='\n'); input(33)
        ## print(df_proof_feat_np.columns,df_proof_nuF_np.columns,sep='\n'); input(33)
        
        ## syntetic df standarized/scaled-.
        arr=np.array([[0.301172,8920.898438,0.253281,168441.601562,0.391016]],dtype=float)
        ## print(arr,np.shape(arr),sep='\n');input(66)
        df_2=pd.DataFrame(data=arr,columns=self.feat_names)
        ## print(df_2);input(77)
        ########## df_proof_feat_np_scaled=self.feat_scal.transform(df_2[self.feat_names]).astype(float)
        
        df_proof_feat_np_scaled=self.feat_scal.transform(df_proof[self.feat_names]).astype(float)
        df_p=pd.DataFrame(data=df_proof_feat_np_scaled,columns=self.feat_names)
        ## print(df_p.mean()); print(df_p.std()); input(33)
        
        ## calculate prediction-.
        df_pred_list=list()
        with torch.no_grad():
            self.model.eval()
            for i_nn, _ in enumerate(range(n_nn)):
                y_pred=self.model(torch.tensor(df_proof_feat_np_scaled,dtype=torch.float).to(torch.float64)).detach().numpy()
                ## print(self.targ_scal.inverse_transform(y_pred)); input(33)
                df_pred=pd.DataFrame(data=self.targ_scal.inverse_transform(y_pred),columns=self.targ_names)
                ## df_pred=pd.DataFrame(data=y_pred),columns=self.targ_names)
                ## df_pred_list.append(pd.DataFrame(data=y_pred,columns=self.targ_names))
                df_pred_list.append(df_pred)
                ## print(df_pred_list)

        return df_pred_list
