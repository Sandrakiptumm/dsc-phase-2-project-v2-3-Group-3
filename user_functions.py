import csv
import pandas as pd
import sqlite3
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.api import OLS
import statsmodels.api as sm
%matplotlib inline
from user_functions import *
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import LabelEncoder


def null(data):
    return data.isna().sum()

def building_model(formula, data_frame):
    """
    takes in formula eg "y ~ x" and your data then outputs a model using the data
    """
    return (sm.formula.ols(formula= formula, data = data_frame))


def plotting_regression_plots(your_model, independent_variable):
    """
    Plots all necessary regression plots to evaluate a model
    """
    fig, ax = plt.subplots(figsize=(8, 6))  # Create a figure and axis
    sm.graphics.plot_regress_exog(your_model, independent_variable, ax=ax)  # Plot regression plots on the axis
    ax.set_xlabel(independent_variable, color='orange')  # Set x-axis label color to orange
    ax.tick_params(axis='x', colors='orange')  # Set x-axis tick color to orange

def drop_duplicates(df, subset=None):
    """
    Drops duplicates from a pandas DataFrame based on a subset of columns and returns the new data frame

   it takes in the df and the subset eg subset = "id"
    """
    return df.drop_duplicates(subset=subset, keep = "first", inplace = True)


def remove_outliers_zscore(df):
    """
    takes in a dataframe and removes outliers from a dataframe using Z-score method.
    
    """
    import numpy as np
    # Calculate Z-scores
    z_scores = np.abs((df - df.mean()) / df.std())
    
    # Identify outliers
    outliers_z = df[(z_scores > 3).any(axis=1)]
    
    # Remove outliers from dataframe
    df_cleaned = df.drop(outliers_z.index)
    return df_cleaned


