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

    fig2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    fig2.show()

build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    fig3 = px.histogram(car_data, x = 'odometer')

    #mostrar un grafico Plotly interactivo
    st.plotly_chart(fig3, use_container_width = True)