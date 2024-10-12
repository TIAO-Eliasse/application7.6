import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
#######""""""""""plotly""""""#######
st.subheader("plotly")

temps=pd.DataFrame({"day":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
                     "temps":[28,27,25,31,32,35,36]})
st.write(temps)
#Diagramme a barre interactive
fig=px.bar(data_frame=temps,y="temps",x="day",
           title="Températures moyennes journalières")

st.plotly_chart(fig)
#Nuage de points intéractifs
#uploaded_file=st.file_uploader("Automobile_data.csv",type=["csv"])
#if uploaded_file is not None:
#import requests
#url = "https://raw.githubusercontent.com/TIAO-Eliasse/application7.6/main/Automobile_data.csv"
#response = requests.get(url)
#with open("Automobile_data.csv", "wb") as file:
    #file.write(response.content)

cars = pd.read_csv("app7/Automobile_data.csv")

st.write(cars)
numeric_cols=cars.select_dtypes(exclude="object").columns.to_list()
categoriecal_cols=cars.select_dtypes(include="object").columns.to_list()
var_x=st.selectbox("choisir la variable en abscisse", numeric_cols)
var_y=st.selectbox("choisir la variable en ordonnée", numeric_cols)
var_categorielle=st.selectbox("choisis la variable categorielle", categoriecal_cols)

fig2=px.scatter(data_frame=cars,x=var_x, y=var_y,
                color=var_categorielle,
                title=str(var_x) +"  vs "+ str(var_y))
st.plotly_chart(fig2)
