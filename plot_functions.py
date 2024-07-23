import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from datetime import datetime


# Convert UNIX timestamps to datetime
def convert_to_datetime(unix_time, offset):
    return datetime.fromtimestamp(unix_time + offset).strftime('%Y-%m-%d %H:%M:%S')


def get_plot(data):
    # Preparing data for plotting
    hourly_data = data['hourly']
    daily_data = data['daily']
    minutely_data = data['minutely']

    hourly_df = pd.DataFrame(hourly_data)
    hourly_df['dt'] = hourly_df['dt'].apply(lambda x: convert_to_datetime(x, data['timezone_offset']))

    daily_df = pd.DataFrame(daily_data)
    daily_df['dt'] = daily_df['dt'].apply(lambda x: convert_to_datetime(x, data['timezone_offset']))

    minutely_df = pd.DataFrame(minutely_data)
    minutely_df['dt'] = minutely_df['dt'].apply(lambda x: convert_to_datetime(x, data['timezone_offset']))
    # Hourly Temperature and Humidity Plot
    fig_hourly_temp_humidity = px.line(hourly_df, x='dt', y=['temp', 'humidity'], title='Hourly Temperature and Humidity')
    fig_hourly_temp_humidity.update_layout(yaxis_title='Temperature (K) / Humidity (%)')

    # Daily Temperature Plot
    fig_daily_temp = go.Figure()
    fig_daily_temp.add_trace(go.Scatter(x=daily_df['dt'], y=daily_df['temp'].apply(lambda x: x['day']), mode='lines+markers', name='Day Temp'))
    fig_daily_temp.add_trace(go.Scatter(x=daily_df['dt'], y=daily_df['temp'].apply(lambda x: x['night']), mode='lines+markers', name='Night Temp'))
    fig_daily_temp.update_layout(title='Daily Temperature', yaxis_title='Temperature (K)', xaxis_title='Date')

    # Minute Precipitation Plot
    fig_minute_precip = px.line(minutely_df, x='dt', y='precipitation', title='Minute-level Precipitation')
    fig_minute_precip.update_layout(yaxis_title='Precipitation (mm)')

    # Wind Speed and Direction Plot
    fig_wind = px.line(hourly_df, x='dt', y='wind_speed', title='Hourly Wind Speed')
    fig_wind.add_bar(x=hourly_df['dt'], y=hourly_df['wind_deg'], name='Wind Direction')
    fig_wind.update_layout(yaxis_title='Wind Speed (m/s)', xaxis_title='Time')

    # Cloud Cover and UV Index Plot
    fig_clouds_uvi = go.Figure()
    fig_clouds_uvi.add_trace(go.Scatter(x=hourly_df['dt'], y=hourly_df['clouds'], mode='lines+markers', name='Cloud Cover (%)'))
    fig_clouds_uvi.add_trace(go.Scatter(x=hourly_df['dt'], y=hourly_df['uvi'], mode='lines+markers', name='UV Index'))
    fig_clouds_uvi.add_trace(go.Scatter(x=hourly_df['dt'], y=hourly_df['visibility']/100, mode='lines+markers', name='Visibility in km'))
    fig_clouds_uvi.update_layout(title='Hourly Cloud Cover and UV Index', yaxis_title='Cloud Cover (%) / UV Index', xaxis_title='Time')
    
    return fig_hourly_temp_humidity, fig_daily_temp, fig_minute_precip, fig_wind, fig_clouds_uvi