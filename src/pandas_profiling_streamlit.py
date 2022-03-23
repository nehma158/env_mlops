import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

# Get data from the link
csv_url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'

data = pd.read_csv(csv_url, sep=';')

# Generate the profile report with Pandas Profiling
profile = ProfileReport(
    data,
    title="Example of summarization of wine data"
)

# Streamlit
st.title("Pandas Profiling in Streamlit!")
st.write(data)
st_profile_report(profile)

# Run with the command:
# streamlit run 'c:\Users\noah-\Documents\01-DSTI\MlOps\env_mlops\src\pandas_profiling_streamlit.py'
