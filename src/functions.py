import pandas as pd
import numpy as np
import scipy.stats as stats
import folium
import matplotlib.pyplot as plt 
plt.style.use('ggplot')
plt.rcParams.update({'font.size': 16, 'font.family': 'sans'})

def select_cols(df, cols):
    '''
    Returns df with specified columns
    
    ARGS:
        df - pd.dataFrame
        cols - list of columns
    '''
    columns_to_drop = []
    for x in df.columns:
        if x not in columns_to_keep:
            columns_to_drop.append(x)
    df.drop(columns_to_drop, inplace=True, axis=1)
    return df

def line_of_best_fit(x,y):
    m, b = np.polyfit(x, y,1)
    line_of_best_fit = m*x+b 
    return line_of_best_fit


if __name__ == '__main__':