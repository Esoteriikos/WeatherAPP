# Weather Application

## Description

A simple weather application providing real-time weather information for any city.

## Tech Stack

- Language: Python
- Weather API: OpenWeatherMap
- Web Framework: Streamlit
- Data Processing: Pandas
- Data Visualization: Plotly
- Hosting Service: Render
- Error Handling Libraries: Python inbuilt, Sentry

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd weather_app
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Set environment variables:
    ```bash
    export OPENWEATHERMAP_API_KEY='your_api_key_here'
    export SENTRY_DSN='your_sentry_dsn_here'
    ```
    On Windows, use:
    ```bash
    set OPENWEATHERMAP_API_KEY=your_api_key_here
    set SENTRY_DSN=your_sentry_dsn_here
    ```

4. Run the application:
    ```bash
    streamlit run app.py
    ```

## Environment Variables

- `OPENWEATHERMAP_API_KEY`: Your API key for OpenWeatherMap
- `SENTRY_DSN`: Your Sentry DSN for error tracking
