#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
##
# class to read config file-.
# @AUTHOR: Fernando Diego Carazo (@buenaluna) -.
# start_date (Fr): mar 23 abr 2024 12:45:21 -03-.
# last_modify (Fr): mar 06 ago 2024 17:41:38 -03-.
#
##
# ======================================================================= INI79

# print(dir()); input(1)

# import the required packages/libraries/modules-.
from os.path import dirname as drn, realpath as rp
from typing import Dict
import yaml

# from ..utils.gen_tools import get_args  as ga
# from ..utils import gen_tools as gt

# main class-.
# 2BeMod: set attributes as private and use getter and setter methods,
#         also delete object after it is used-.
class Config():
    '''
        A class to load config file-.
    ...
    Attributes (only an example, 2BeCompleted-.)
    ----------
    name : str
        first name of the person
    Methods  (only an example, 2BeCompleted-.)
    -------
    info(additional=""):
        Prints the person's name and age.
    '''
    
    def __init__(self, cfg: Dict):
        ''' constructor '''
        self.config = cfg  # in
        ## out-.
        self.save = self.config['gen_options']['save']  # 2save or not the figures-.
        self.dir_save = self.config['gen_options']['dir_save']  # 2set path save figures-.
        self.dir_results = self.config['gen_options']['dir_results']  # 2set path save figures-.
        self.dir_logs = self.config['gen_options']['dir_logs']  # 2set path save figures-.
        self.vars_names = self.config['gen_options']['vars_names']
        self.feat_names = self.config['gen_options']['feat_names']
        self.targ_names = self.config['gen_options']['targ_names']
        self.n_nn = self.config['gen_options']['nnn']
        self.quart = self.config['gen_options']['quart']

        # 3- Scaler/Standarize, etc. dataset-.
        self.scale_targ = self.config['scaler']['scale_targ']
        self.scaler_type = self.config['scaler']['type_sca']
        self.scaler_test_size = self.config['scaler']['test_size']
        self.scaler_shuffle = self.config['scaler']['shuffle']
        self.scaler_save = self.config['scaler']['save']

        # 2-2- train_test_split_torchDataset_torchDataLoader-.
        self.rand = self.config['train_test_torch']['rand']
        self.test_frac = self.config['train_test_torch']['test_frac']
        self.shuffle = self.config['train_test_torch']['shuffle']
        # torch.dataLoader section-.
        self.batch_size = self.config['train_test_torch']['batch_size']  # torch.DataLoader-.
        self.shuffle_torch = self.config['train_test_torch']['shuffle_torch']  # torch.DataLoader-.
        
        # self.currentdir=drn(rp(__file__))
        # self.config_file_path = '/Users/Fernando/scratch/elasAnys/2testModels/config_file.yaml'
        # self.root= drn(self.currentdir)
        # self.root_ds= self.config['dataset']['ds_path']
        
        # 2-2- Dataset names-.
        # datasets (used to train and test)-.
        self.ds_path = self.config['dataset']['path']
        self.ds_file = self.config['dataset']['name']

        # 5- PytorcModel/s-.
        # general parameters (for FFNN,BNNbnn,MAML, ENSEMBLE, etc)
        # NN general option (deep or shallow NN)-.
        self.DL_name = self.config['model']['name']
        self.layers_architecture = self.config['model']['layers_architecture']
        self.lr = self.config['model']['lr']
        self.optimizer = self.config['model']['optimizer']
        self.loss = self.config['model']['loss']
        self.epochs = self.config['model']['epochs']
        self.weight_decay = self.config['model']['weight_decay']
        self.momentum = self.config['model']['momentum']
        self.plot_loss = self.config['model']['plot_loss']
        self.model_loss_save = self.config['model']['save']
        # for BayesNeuralNetwork (with torchbnn)
        self.kl_l = self.config['model']['kl_l']
        self.kl_w = self.config['model']['kl_w']
        # for MAML Pytorch (from scratch)
        self.optimizer_inner = self.config['model']['optimizer_inner']
        self.num_outer_upd = self.config['model']['num_outer_upd']
        self.num_inner_upd = self.config['model']['num_inner_upd']
        self.lr_outer = self.config['model']['lr_outer']
        self.lr_inner = self.config['model']['lr_inner']
        # for Pytorch Ensemble models (torchensemble
        self.num_est = self.config['model']['n_e']

        # 6- NN's Hyperparameter Optimziation-.
        # for hyperparamenter optimization-.
        self.hyper_optim_apply = self.config['hyper_optim']['apply']
        self.hyper_optim_name = self.config['hyper_optim']['name']
        self.plot_optim_hist = self.config['hyper_optim']['plot_optim_hist']
        self.test = self.config['hyper_optim']['test']
        self.optuna_epochs = self.config['hyper_optim']['epochs']

        
if __name__ == '__main__':
    # config_file_path ='/home/fdcarazo/my_github/pyroYieldPred/config_file.yaml'
    config_file_path = '/home/fcarazo/my_github/TG_ML/dl_model/config_file_all_withoutOH.yaml'
    with open(config_file_path, 'r') as f: config = yaml.safe_load(f)
    cfg_obj = Config(config)
    print(cfg_obj.__dir__(), dir(cfg_obj), sep='\n'*2)
    print('{}{}'.format('\n'*3, cfg_obj.__dict__))
    print(cfg_obj.scaler_type, cfg_obj.DL_name, sep='\n')
else:
    print('{0} imported as Module'.format(__file__.split('/')[-1]))
