# Import the required libraries
import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Load the data
Athletes = pd.read_csv('Athletes.csv')

# Dropping unnecessary columns
Athletes.drop(['Wikipedia Page', 'dbpedia Page', 'Image', 'Description'], axis=1, inplace=True)

# Create the Header
st.header('Highest Paid Athletes')
st.dataframe(Athletes)

# Plot the histogram
fig = px.histogram(Athletes, x='Total Pay', 
                   nbins=50, color='Sport', 
                   title='Histogram of Total Pay per Sport')
st.plotly_chart(fig)


# Plot the scatterplot
# Checkbox to select the sport
if not st.checkbox('Show Sport', value=False):

    scatterplot = px.scatter(Athletes, x='Height (cm)', 
           y='Endorsements', 
           title='Scatterplot of Height vs Endorsements')

    st.plotly_chart(scatterplot)
else:
    scatterplot = px.scatter(Athletes, x='Height (cm)', 
           y='Endorsements', 
           color='Sport',
           title='Scatterplot of Height vs Endorsements')

    st.plotly_chart(scatterplot)


# Checkbox to select the gender
by_gender = st.checkbox('Select Gender')

# Filter data based on checkbox
if by_gender:
    # Select gender using a selectbox
    selected_gender = st.radio('Select Gender', Athletes['Gender'].unique())
    
    # Filter data for the selected gender
    filtered_athletes = Athletes[Athletes['Gender'] == selected_gender]
else:
    filtered_athletes = Athletes

# Calculate percentages
total_athletes = len(filtered_athletes)
country_counts = filtered_athletes['Nation'].value_counts()
country_percentages = (country_counts / total_athletes) * 100

# Convert to DataFrame
country_percentage_df = country_percentages.reset_index()
country_percentage_df.columns = ['Country', 'Percentage (%)']

# Create a bar chart
fig4 = px.bar(
    country_percentage_df, 
    x='Country', 
    y='Percentage (%)', 
    title='Percentage of Athletes by Country', 
    color='Country'
)

# Display the plot
st.plotly_chart(fig4)    










