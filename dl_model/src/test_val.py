#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
##
# Train-Test split of dataset-.
# @AUTHOR: Fernando Diego Carazo (@buenaluna) -.
#
# start_date (Fr): Mon Mar 18 21:52:48 CET 2024-.
# last_modify (Fr): mar 06 ago 2024 14:25:35 -03-.
##
# ======================================================================= INI79

# print(dir()); input(1)

# import packages/libraries/modules-.
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# import numpy as np

class test_val():
    def __init__(self, df, feat_var, targ_var):
        self.df= df
        self.feat_var, self.targ_var= feat_var, targ_var

    def train_val(self, rand, val_frac, shuff=True):
        X_train, X_val, y_train, y_val= train_test_split(
            self.df.loc[:, self.feat_var],
            self.df.loc[:, self.targ_var],
            test_size= val_frac,
            shuffle= shuff,
            random_state= rand)
        return X_train, X_val, y_train, y_val

    def scaler(self, scaler, X_train, X_val, y_train, y_val):
        scaler= eval(scaler)
        X_train= scaler.fit_transform(X_train)
        X_val= scaler.transform(X_val)
        y_train= scaler.fit_transform(y_train)
        y_val= scaler.transform(y_val)

        '''
        print(np.mean(X_train), np.mean(X_val),
              np.mean(y_train), np.mean(y_val), sep='\n')
        print(np.std(X_train), np.std(X_val),
              np.std(y_train), np.std(y_val), sep='\n')
        '''
        return X_train, X_val, y_train, y_val

# main (to load as module)-.
if __name__ == '__main__':
    pass
