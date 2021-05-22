import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import os


def get_file_path(file_name):
    responses_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(responses_dir, file_name)
    return file_path


def data_reader(file_name):
    file_contents = pd.read_csv(get_file_path(file_name))
    return file_contents


def array_of_data(file_contents):
    pass


def daily_average(file_contents):
    pass
