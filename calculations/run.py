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
    if sfname in ['bt-score', 'bt-screen', 'bt-dock', 'svm', 'mars', 'rf']:
      return ['xscore','affiscore', 'rfscore']
    elif sfname == 'rf-score':
      return ['xscore','affiscore', 'rfscore']
    elif sfname == 'x-score':
      return ['xscore','affiscore', 'rfscore']

#
# Get the results for a given SF and task
#
def run_results(scoring_fname, task_name, num_complexes, folder_pref=''):
    sfname = scoring_fname.lower()
    task = task_name.lower()
    verbose = True
    n_cpus = None
    preds_ofname = 'results/prediction_results_'+ scoring_fname + folder_pref + '.csv'
    perf_ofname = 'results/performance_results_'+ scoring_fname + folder_pref + '.csv'

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


    predictions, performance = train_test_model(task, sfname, train, test, model_params, num_complexes)

    print('\nPerformance of %s on the %sing task:'%(sfname, task))
    print(performance.to_string(index=False))

    if verbose:
      print('Writing performance statistics to ' + perf_ofname)
    performance.to_csv(perf_ofname, index=False)

#
# main function
#
def main():
    # get results for number of training set less than 3250
    for num in [500, 1000, 1500, 2000, 2500, 3000, 3250]:
        for sf in ['svm', 'bt-score', 'rf-score', 'mars', 'x-score']:
            folder_pref = '_XAR_' + str(num)
            run_results(sf, 'score', num,  folder_pref)

#
# Run Main Functions
#
if __name__== '__main__':
    main()
