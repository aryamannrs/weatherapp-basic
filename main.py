import requests


def get_weather(city):
    API_KEY = "ENTER KEY" 
    BASE_URL = "http://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": city,  
        "aqi": "yes"  
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  

        data = response.json()
        location = data["location"]["name"]
        region = data["location"]["region"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        aqi = data["current"]["air_quality"]

        pm2_5 = aqi.get("pm2_5", 0)  

        if pm2_5 <= 50:
            aqi_category = "Good"
        elif pm2_5 <= 100:
            aqi_category = "Moderate"
        elif pm2_5 <= 150:
            aqi_category = "Unhealthy for Sensitive Groups"
        elif pm2_5 <= 200:
            aqi_category = "Unhealthy"
        elif pm2_5 <= 300:
            aqi_category = "Very Unhealthy"
        else:
            aqi_category = "Hazardous"

        print(f"Weather in {location}, {region}, {country}:\n"
              f"Temperature: {temp_c}°C \n",
              f"Humidity: {humidity}%\n",f"AQI: {pm2_5}, {aqi_category}\n")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError:
        print("Invalid response received. Please check the city name or API key.")
while True:
    if __name__ == "__main__":
        city_name = input("Enter the city name: ")
        get_weather(city_name)
