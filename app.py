import streamlit as st
from weather import get_weather

st.set_page_config(
    page_title="Weather Forecast App",
    page_icon="🌤️"
)

st.title("🌤️ Weather Forecast App")
st.write("Enter a city name to get live weather details.")

city = st.text_input("City Name")

if st.button("Get Weather"):
    if city.strip() == "":
        st.warning("Please enter a city name.")
    else:
        result = get_weather(city)

        if "error" in result:
            st.error(result["error"])
        else:
            st.success(f"Weather in {result['city']}")

            st.metric("🌡️ Temperature", f"{result['temperature']} °C")
            st.write(f"💧 **Humidity:** {result['humidity']}%")
            st.write(f"☁️ **Condition:** {result['condition']}")
            st.write(f"🌬️ **Wind Speed:** {result['wind_speed']} m/s")
