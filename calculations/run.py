#!/usr/bin/env python

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import argparse
import pandas as pd
import numpy as np
import timeit
from read_plc_data import read_plc_data
from model_utils import train_test_model
from train_test_task_specific_sfs import get_ba_data
import os
import sys
import multiprocessing

#
# Set descriptors based on sf selection
#
def set_descriptors(sfname):
    if sfname in ['bt-score', 'bt-screen', 'bt-dock']:
      return ['xscore', 'affiscore', 'rfscore', 'gold',
                        'repast', 'smina', 'chemgauss', 'autodock41',
                        'ligscore', 'dsx', 'cyscore', 'padel',
                        'nnscore', 'retest', 'ecfp', 'dpocket']
    elif sfname == 'rf-score':
      return ['rfscore']
    elif sfname == 'x-score':
      return ['xscore']

#
# Get the results for a given SF and task
#
def run_results(scoring_fname, task_name):
    sfname = scoring_fname.lower()
    task = task.lower()
    verbose = True
    n_cpus = None
    preds_ofname = 'prediction_results.csv'
    perf_ofname = 'performance_results.csv'

    # Descriptors to use
    descriptor_sets = set_descriptors(sfname)

    rem_y = sfname in ['rf-score', 'x-score']

    n_cpus = multiprocessing.cpu_count() if n_cpus is None else n_cpus
    model_params = {'n_cpus': n_cpus}

    # Training data path
    tr_dpath = os.path.join('data', 'input', task, 'primary-train')
    # Test data path
    ts_dpath = os.path.join('data', 'input', task, 'core-test')

    # TRAIN
    train, ftrs_formula = read_plc_data(task, descriptor_sets=descriptor_sets,
                                        rem_y=rem_y, data_path=tr_dpath,
                                        verbose=verbose)

    #TEST
    test, ftrs_formula = read_plc_data(task, descriptor_sets=descriptor_sets,
                                       rem_y=rem_y, data_path=ts_dpath,
                                       verbose=verbose)

    if ((sfname in ['rf-score', 'x-score']) or (sfname == 'bt-score' and task != 'score')):
      train = get_ba_data(train, task)

'''
    predictions, performance = train_test_model(task, sfname, train, test, model_params)

    print('\nPerformance of %s on the %sing task:'%(sfname, task))
    print(performance.to_string(index=False))

    if verbose:
      print('Writing predictions to ' + preds_ofname)
    predictions.to_csv(preds_ofname, index=False)

    if verbose:
      print('Writing performance statistics to ' + perf_ofname)
    performance.to_csv(perf_ofname, index=False)
'''

#
# main function
#
def main():
    run_results('bt-score', 'score')

#
# Run Main Functions
#
if __name__== '__main__':
    main()
