# 🌤️ Weather Forecast App

A simple web application to check live weather for any city in the world.

## Features
- 🌡️ Real-time temperature
- 💧 Humidity percentage
- ☁️ Weather conditions
- 🌬️ Wind speed

## Live Demo
[Open Weather App on Streamlit Cloud](https://weather-forecast-app.streamlit.app)

## Quick Start (Local)

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/weather-forecast-app.git
cd weather-forecast-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Getting Your Own API Key (Optional)

For better reliability with higher usage:

1. Go to [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Copy your API key from the API keys dashboard
4. Replace the API key in `.env` file

## Configuration Files

- **requirements.txt** - Python dependencies
- **.env** - Environment variables for local testing (API key)
- **.streamlit/config.toml** - Streamlit configuration
- **.streamlit/secrets.toml** - Local Streamlit secrets (for testing)
- **.gitignore** - Files to exclude from Git

## Deploying to Streamlit Cloud

See [DEPLOYMENT.md](DEPLOYMENT.md) for step-by-step instructions.

## Project Structure

```
weather-forecast-app/
├── app.py                    # Streamlit web app (main file)
├── main.py                   # Desktop Tkinter app (optional)
├── weather.py                # API logic
├── requirements.txt          # Python dependencies
├── .env                       # Environment variables
├── .gitignore                # Git ignore rules
├── .streamlit/
│   ├── config.toml          # Streamlit configuration
│   └── secrets.toml         # Local secrets
└── README.md                 # This file
```

## Limitations (Free Tier)

- **API Calls:** 1,000 per day (OpenWeatherMap free tier)
- **Memory:** 1 GB RAM
- **Inactivity:** App sleeps after 7 days without traffic
- **Concurrency:** 1 user at a time (others queue)

## Troubleshooting

### "City not found" error
- Check spelling of city name
- Try a major city (e.g., "London", "New York")

### "No internet connection" error
- Check your internet connectivity
- OpenWeatherMap API might be temporarily down

### "Error running app" error
- Ensure API key is set correctly in Streamlit Secrets
- Check that all dependencies are installed
- Verify `app.py` is the main file

## License
MIT License - Feel free to use this for your projects!

## Support
For issues, create an issue on GitHub or contact the maintainer.

