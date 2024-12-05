# STEP1: Instalamos las librerias necesarias
# pip install streamlit plotly requests pandas

# STEP2: Importamos las librerias
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# STEP3: Funcion para obtener la previsión del tiempo
def get_weather_forecast(lat, lon):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data from Open-Meteo API: {e}")
        return None

# STEP4: Aplicacion streamlit
st.title("Weather Forecast App")
st.write("Obtenga el pronóstico del tiempo para cualquier ubicación utilizando Open-Meteo API.")
st.write("https://open-meteo.com/en/docs")
st.write("https://streamlit.io/: Para crear aplicaciones web interactivas")

# STEP5: Organizamos las entradas y el botón en columnas para evitar desplazamiento vertical
# Ej.: Castellon --> lat = 39.98567, long=-0.04935
col1, col2 = st.columns([1, 1])
with col1:
    lat = st.number_input("Introducir Latitud:", value=0.0, format="%.6f", step=0.000001)
with col2:
    lon = st.number_input("Introducir Longitud:", value=0.0, format="%.6f", step=0.000001)

fetch_button = st.button("Conseguir el pronóstico")


# STEP6: Validamos lo que introduce el usuario
if lat < -90 or lat > 90:
    st.error("Latitude must be between -90 and 90.")
if lon < -180 or lon > 180:
    st.error("La longitud debe estar entre - 180 y 180.")

# STEP7: Busca la previsión meteorológica
if fetch_button and (-90 <= lat <= 90) and (-180 <= lon <= 180):
    with st.spinner("Datos de búsqueda..."):
        data = get_weather_forecast(lat, lon)
    if data:
        hourly_data = data['hourly']['temperature_2m']
        times = pd.to_datetime(data['hourly']['time'])

        st.write(f"Previsión del tiempo para Latitud: {lat}, Longitud: {lon}")

        # Crea un DataFrame para visualización
        forecast_data = {'Tiempo': times, 'Temperatura (°C)': hourly_data}
        forecast_df = pd.DataFrame(forecast_data)

        # Muestra los datos en un gráfico de líneas usando la libreria Plotly
        fig = px.line(forecast_df, x='Tiempo', y='Temperatura (°C)', title='Pronostico de temperatura')
        fig.update_layout(xaxis_title='Tiempo', yaxis_title='Temperatura (°C)')
        st.plotly_chart(fig)

# STEP8: Ejecuta la App
#Para que el programa encuentre la libreria streamlit:
#export PATH="/home/usuario/.local/bin/:$PATH" <-- abajo en el recuadro del terminal
#streamlit run weather_app.py <-- abajo en el recuadro del terminal