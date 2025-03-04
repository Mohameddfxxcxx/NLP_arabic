'''
import pandas as pd
import os
from sys import path


def check_results():
    '''Compares the exp file with templated pre_generated results file.
       To compare the reproducibility of the code.

        Args:
            exp_file: the file which is extracted after running main_test.
    '''

    result1 = pd.read_csv('lib/All_Experiments_Results_template.csv')
    result2 = pd.read_csv('All_Experiments_Results.csv')

    try:
        pd.testing.assert_frame_equal(result1, result2, check_dtype=False)
        return True
    except:
        return False

'''
# The template file 
check_results()
'''
