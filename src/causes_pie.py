import pandas as pd
import numpy as np
import scipy.stats as stats
import folium
import matplotlib.pyplot as plt 
plt.style.use('ggplot')
plt.rcParams.update({'font.size': 16, 'font.family': 'sans'})

import functions as fn 


if __name__ == '__main__':
    df = pd.read_csv('../data/CU_Anschutz_maternal-mortality-causes.csv')
    df = fn.drop_empty_rows(df)
    df['Cause of death'] = ['Suicide', 'Drug overdose', 'Injury/Accident',
                             'Homicide', 'Cardiac', 'Pregnancy disorders',
                            'Infection', 'Stroke', 'Blood clot', 'Other non-medical']

    
    labels = df['Cause of death']
    sizes = df['Number of pregnancy- associated deaths']
    explode = (0.3,0.3,0,0,0,0,0,0,0,0)

    fig, ax=plt.subplots(figsize=(15,10))
    ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')
    ax.set_title('Causes of Pregnancy-Associated Deaths\n 2008-2016')
    plt.show()
    plt.savefig('../images/causes_pie.png')
