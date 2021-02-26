import pandas as pd
import numpy as np
import scipy.stats as stats
import folium
import matplotlib.pyplot as plt 
plt.style.use('ggplot')
plt.rcParams.update({'font.size': 16, 'font.family': 'sans'})

import functions as fn 

if __name__ == '__main__':
    # read in SAMHSA facilities & minor adjustments
    df1 = pd.read_csv('../data/SAMHSA_Colorado_Substance_Abuse_and_Mental_Health_Service_Providers.csv')
    df1 = df1.rename({'Type_':'Type'}, axis=1)
    
    # read in Special Connection provider facilities and adjust
    df2 = pd.read_csv('../data/Special_Connections_Providers_January_2021.csv')
    columns_to_keep = ['Provider', 'Area of Service', 'Phone']
    df2 = fn.select_cols(df2, columns_to_keep)
    df2 = fn.drop_empty_rows(df2)
    df2 = df2.rename({ 'Provider': 'Special Connection Provider' }, axis=1)
    
    # prep dataframes for merge on Phone records
    df2 = fn.phone_dashes(df2)
    df2.loc[3,'Phone']    = '970-350-5330'
    df1.loc[55,  'Phone'] = '970-245-4213'
    df1.loc[321, 'Phone'] = '970-245-4213'
    df1.loc[321, 'Phone'] = '970-245-4213'
    df1.loc[436, 'Phone'] = '303-734-5000'
    df1.loc[465, 'Phone'] = '720-623-0747'

    # merege dataframes
    df_joined = pd.merge(df1,df2, on='Phone', how='left')
    df_joined['Special Connection Provider'] =df_joined['Special Connection Provider'].fillna(0)
    df_joined['Special_Connection_Approved'] = df_joined['Special Connection Provider'].astype(bool)
    
    # map all locations 
    df_map = folium.Map(location=[39.6393556, -105.0362754],zoom_start=7)

    for Y,X, Provider_Name in zip(df_joined['Y'], df_joined['X'], df_joined['Provider_Name']):
        folium.Marker(
            [Y,X],
            popup=Provider_Name,
            icon=folium.Icon(color='blue')
        ).add_to(df_map)
    df_map

    # prep df in order map transitional housing & special connections
    # th is for transitional housing that utilize medication applied treatment
    th = df_joined[df['Transitional_Housing']=='Transitional housing or halfway house']
    th = th[["Provider_Name", 'Y', 'X', 'City', 'Website_URL', 'Opiod_Treatment_Settings','Special_Connection_Approved','LATITUDE', 'LATITUDE']]
    th = th[trans_housing['Opiod_Treatment_Settings'] != 'Does not treat opioid addiction']
    th = th[trans_housing['Opiod_Treatment_Settings'] != 'Do not use medication for opioid addiction']
    th

    # sc is for special connections the state medicaid approved extended care facilities
    sc = df_joined[['Type','Provider_Name', 'Y','X','City']][df['Special_Connection_Approved']==True]
    
    
    # map transitional housing & special connections

    sc_and_th= folium.Map(location=[39.6393556, -105.0362754],zoom_start=7)

    #special connections approved facilities: 
    for Y,X, Provider_Name in zip(sc['Y'], sc['X'], sc['Provider_Name']):

    folium.Marker(
            [Y,X],
            popup=Provider_Name,
            icon=folium.Icon(color='pink',icon="star")
        ).add_to(sc_and_th)


    #map residential treatment facilities
    for Y,X, Provider_Name in zip(trans_housing['Y'], trans_housing['X'],trans_housing['Provider_Name']):

        folium.Marker(
            [Y,X],
            popup=Provider_Name,
            icon=folium.Icon(icon="home")
        ).add_to(sc_and_th)

    sc_and_th

    #special connections approved facilities: 
    sc_map = folium.Map(location=[39.6393556, -105.0362754],zoom_start=7)
    for Y,X, Provider_Name in zip(sc['Y'], sc['X'], sc['Provider_Name']):

    folium.Marker(
            [Y,X],
            popup=Provider_Name,
            icon=folium.Icon(color='pink',icon="star")
        ).add_to(sc_and_th)
    sc_map



    