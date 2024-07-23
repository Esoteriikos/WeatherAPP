import streamlit as st
import pandas as pd

from weather_api import fetch_coordinates, fetch_weather
import sentry_sdk
import os
from datetime import datetime
from plot_functions import get_plot, convert_to_datetime


# Initialize Sentry for error tracking
sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN'),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

# Load environment variables
API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

if not API_KEY:
    st.error("API key is not set. Please set the OPENWEATHERMAP_API_KEY environment variable.")
    st.stop()

def display_weather(data):

    current = data['current']
    st.write(f"**Temperature:** {current['temp']}°C")
    st.write(f"**Feels like:** {current['feels_like']}°C")
    st.write(f"**Sunrise:** {convert_to_datetime(current['sunrise'], data['timezone_offset'])}")
    st.write(f"**Sunset:** {convert_to_datetime(current['sunset'], data['timezone_offset'])}")
    st.write(f"**UV Index:** {current['uvi']}")
    st.write(f"**Pressure:** {current['pressure']} hPa")
    st.write(f"**Humidity:** {current['humidity']}%")
    st.write(f"**Visibility:** {current['visibility']}m")
    st.write(f"**Wind Speed:** {current['wind_speed']} m/s at {current['wind_deg']}°")
    st.write(f"**Weather Conditions:** {current['weather'][0]['description']}")
    st.write(f"**Cloud Cover:** {current['clouds']}%")

    # Streamlit App 
    fig_hourly_temp_humidity, fig_daily_temp, fig_minute_precip, fig_wind, fig_clouds_uvi= get_plot(data)
    st.plotly_chart(fig_hourly_temp_humidity)
    st.plotly_chart(fig_daily_temp)
    st.plotly_chart(fig_minute_precip)
    st.plotly_chart(fig_wind)
    st.plotly_chart(fig_clouds_uvi)


def main():
    st.title("Weather Application")

    city = st.text_input("Enter city name:")

    if city:
        try:
            lat, lon = fetch_coordinates(city, API_KEY)
            weather_data = fetch_weather(lat, lon, API_KEY)
            st.success(f"Weather data for {city} retrieved successfully!")
            display_weather(weather_data)
        except Exception as e:
            st.error(f"Error fetching weather data. Please check the city name.")


if __name__ == "__main__":
    main()
