import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.graph_objects as go


def app_launcher():
    st.title("Nifty moving avg strategy")
    ma_period = st.sidebar.slider(label="Select Moving average period",min_value=5,max_value=200,step=1)
    investment_amount = st.sidebar.number_input(label="Investment amount",min_value=100,step=1000,value=100)
    holding_period = st.sidebar.number_input(label="Investment period (in Years)",min_value=1,max_value=11)
    starting_year = st.sidebar.number_input(label="Starting Year",min_value=2010,max_value=2021-holding_period)
    fig = computation(starting_year,holding_period,ma_period)
    st.plotly_chart(fig,use_container_width=False)


def data_cleaning(starting_year,holding_period):
    df = pd.read_excel("NIFTYBEES.xlsx")
    df = df.bfill(axis='rows')
    df = df[df['Date']<=datetime.datetime((starting_year + holding_period),12,31)]
    df = df[df['Date']>=datetime.datetime(starting_year,1,1)]
    return df
def computation(starting_year,holding_period,ma_period):
    df = data_cleaning(starting_year,holding_period)
    df['Moving_avg'] = df['Close'].rolling(window=ma_period).mean()
    ma_df = df[df['Moving_avg']>=0]
    print(ma_df.head())
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Close']))
    fig.add_trace(go.Scatter(x=ma_df['Date'], y=ma_df['Moving_avg']))
    fig.update_layout(height = 600,width = 1200)
    return fig


#computation()
#data_cleaning()
app_launcher()