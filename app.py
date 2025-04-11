import pandas as pd
import plotly.express as px
import streamlit as st
dogs = pd.read_csv('dog_intelligence.csv')
st.dataframe(dogs)

