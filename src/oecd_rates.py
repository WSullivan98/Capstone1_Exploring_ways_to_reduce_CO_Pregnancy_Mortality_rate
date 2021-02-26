import pandas as pd
import numpy as np
import scipy.stats as stats
import folium
import matplotlib.pyplot as plt 
plt.style.use('ggplot')
plt.rcParams.update({'font.size': 16, 'font.family': 'sans'})

import functions as fn 


if __name__ == '__main__':
    df = pd.read_csv('../data/OECD_Maternal_Mortality_rate.csv')
    df = df.rename({"2018":"Rates"},axis=1)
    q1 = df.quantile(.25)
    q3 = df.quantile(.75)

    df = df.sort_values('Rates', ascending=False) 
    fig, ax =plt.subplots(figsize=(20,13))
    x = df['Rates']
    y = df['Country']
    ax.set_title("OECD Pregnancy Mortality rates\n")
    ax.set_xlabel('Mortalities per 100,000 Births')
    ax.set_ylabel('OECD Countries')
    bars = ax.barh(y, width=x, height=0.4, color='b')
    bars[2].set_color('r')
    #plt.show()

    plt.savefig('../images//OECD_Pregnancy_Mortality_Rates.png')