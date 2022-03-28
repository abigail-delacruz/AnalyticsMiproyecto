import pandas as pd
import streamlit as st

df = pd.read_csv("DATA\Churn_Modelling.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files

st.title("Reporte de fuga de clientes bancarios")  # add a title
st.write(df)  # visualize my dataframe in the Streamlit app

fig, ax = plt.subplots()
  df.hist(
    bins=8,
    column="Age",
    grid=False,
    figsize=(8, 8),
    color="#86bf91",
    zorder=2,
    rwidth=0.9,
    ax=ax,
  )
  st.write(fig)