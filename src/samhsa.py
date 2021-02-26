import pandas as pd
import numpy as np
import scipy.stats as stats
import folium
import matplotlib.pyplot as plt 
plt.style.use('ggplot')
plt.rcParams.update({'font.size': 16, 'font.family': 'sans'})

import functions as fn 

if __name__ == '__main__':
    df1 = pd.read_csv('../data/SAMHSA_Colorado_Substance_Abuse_and_Mental_Health_Service_Providers.csv')
    df1 = df1.rename({'Type_':'Type'}, axis=1)
    
    df2 = pd.read_csv('../data/Special_Connections_Providers_January_2021.csv')
    columns_to_keep = ['Provider', 'Area of Service', 'Phone']
    df2 = fn.select_cols(df2, columns_to_keep)
    df2 = fn.drop_empty_rows(df2)
    df2 = df2.rename({ 'Provider': 'Special_Connection_Provider' }, axis=1)


    print(df2)