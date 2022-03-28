import pandas as pd
import streamlit as st

df = pd.read_csv('..\DATA\Churn_Modelling.csv')  # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files

st.title("Reporte de fuga de clientes bancarios")  # add a title
st.write(df)  # visualize my dataframe in the Streamlit app

