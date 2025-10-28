import streamlit as st
import pandas as pd
from vega_datasets import data


import matplotlib.pyplot as plt

#Sets the page configuration to use as much space as possible
st.set_page_config(layout='wide')

#Creates a title
st.title("Statistics on Adults")
st.divider()

@st.cache_data #Caches the data so it does not waste time reading the data multiple times. 
def load_data():
    df = pd.read_csv('adult.csv')
    return df
df = load_data()

st.header('Data for Adults')

# Creates a table to display the csv
df_st = st.data_editor(df)

c1, c2 = st.columns([1,1]) #Splits the screen into 2 columns
with c1:
    df1 = pd.DataFrame()
    df1=df['income'].value_counts()
    st.header('Number of Individuals per Income Range')
    st.bar_chart(df1) #Creates a bar chart with the number of individuals per income range

# Example from Matplotlib.ipynb
with c2: 
    fig, ax = plt.subplots(figsize=(9, 4)); # resizes the plot
    x = df['workclass'].unique() # getting all the unique values in the column
    y = []

    for workclass in x:
        y.append(df[df['workclass'] == workclass].shape[0]) # getting the number of instances for each class

    ax.stem(x, y)
    plt.xlabel('Workclass')
    plt.title('Distribution of Workclass')

    st.pyplot(fig) #Displays a numpy array

breakp = 'oint'
