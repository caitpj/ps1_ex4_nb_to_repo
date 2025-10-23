# Packages to load at start
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier

# TODO: Add all hard coded parameters like file paths or model parameters here
TRAIN_PATH = "train.csv"

# read the data
def data_load(TRAIN_PATH):
    train_df = pd.read_csv(TRAIN_PATH)
    return train_df

# TODO: move to orchestration script?
train_df = data_load(TRAIN_PATH)