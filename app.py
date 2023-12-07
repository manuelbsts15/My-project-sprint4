import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('/Users/Claudio/documents/My-project-sprint4/vehicles_us.csv')  # leer los datos
hist_button = st.button('Constriur histograma') # crear boton

if hist_button : #al hacer click en el boton
    #escribir mensaje
    st.write('Creacion de un histograma para el conjunto de datos de anuncios de venta de coches')

    #crear un histograma
    fig = px.histogram(car_data, x = 'odometer')

    #mostrar un grafico Plotly interactivo
    st.plotly_chart(fig, use_container_width = True)
    