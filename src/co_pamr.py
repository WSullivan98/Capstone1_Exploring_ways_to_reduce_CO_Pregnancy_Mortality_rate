import pandas as pd
import numpy as np
import scipy.stats as stats
import folium
import matplotlib.pyplot as plt 
plt.style.use('ggplot')
plt.rcParams.update({'font.size': 16, 'font.family': 'sans'})

import functions as fn 


# Purpose of the script is to read in data from the Anschutz study and produce visuals


if __name__ == '__main__':

    df = pd.read_csv('../data/CU_Anschutz_PAMR_2014-2016.csv')
    columns_to_keep = ['year','pamr']
    df =  fn.select_cols(df, columns_to_keep )
    
    fig, ax = plt.subplots(figsize=(12,7))
    x= df['year'] 
    y= df['pamr']   
    
    ax.set_ylim([10,60])
    ax.yaxis.set_ticks(range(10, 65,5)) 
    plt.plot(x,fn.line_of_best_fit(x,y), label='Trend line',linestyle='dashed')
    ax.set_xlabel('Years')
    ax.set_ylabel('Mortality per 100,000 pregnancies\n')
    ax.set_title("Colorado's Pregnancy Associated Mortality Rate \n")
    ax.plot(x,y, label='PAMR')
    plt.legend()
    #plt.show()
    plt.savefig('../images/co_pamr.png')
