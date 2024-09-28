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
cars=pd.read_csv("Automobile_data.csv")
st.dataframe(cars)
numeric_cols=cars.select_dtypes(exclude="object").columns.to_list()
categoriecal_cols=cars.select_dtypes(include="object").columns.to_list()
var_x=st.selectbox("choisir la variable en abscisse", numeric_cols)
var_y=st.selectbox("choisir la variable en ordonnée", numeric_cols)
var_categorielle=st.selectbox("choisis la variable categorielle", categoriecal_cols)

fig2=px.scatter(data_frame=cars,x=var_x, y=var_y,
                color=var_categorielle,
                title=str(var_x) +"  vs "+ str(var_y))
st.plotly_chart(fig2)