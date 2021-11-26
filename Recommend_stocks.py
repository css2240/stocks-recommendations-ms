import streamlit as st
import pandas as pd
import numpy as np
import datetime


def app_launcher():
    st.title("Stocks Recommendation (MS)")
    recomendation_date = st.sidebar.date_input(label="Date of recommendations",min_value=datetime.date(2021,1,1),max_value=datetime.date.today())
    investment_amount = st.sidebar.number_input(label="Investment amount",value=10000,step=1000)
    number_of_stocks = st.sidebar.number_input(label="Number of stocks to be recommended",value=5,min_value=5,max_value=12,step=1)

app_launcher()