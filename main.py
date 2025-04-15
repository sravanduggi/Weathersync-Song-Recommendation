from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# Load API keys from environment variables
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")



@app.get("/")
def read_root():
    return {"message": "Welcome to the Mood-Weather-Song Recommendation API"}

@app.get("/recommendation/")
def get_recommendation(mood: str, city: str):
    """
    Endpoint to get a song recommendation based on user's mood and city weather.
    """
    try:
        # Fetch weather data
        weather_data = fetch_weather(city)
        if not weather_data:
            raise HTTPException(status_code=404, detail="City not found or weather data unavailable")

        # Match mood with weather
        weather_condition = weather_data.get("weather")[0].get("main").lower()
        if not mood_matches_weather(mood.lower(), weather_condition):
            return {"message": "Mood does not match the current weather in the city"}

        # Fetch song recommendation
        song = fetch_song_recommendation(mood)
        if not song:
            raise HTTPException(status_code=404, detail="No song recommendation found")

        return {
            "city": city,
            "weather": weather_condition,
            "mood": mood,
            "recommended_song": song
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def fetch_weather(city: str):
    """
    Fetch current weather data for the given city using OpenWeatherMap API.
    OpenWeatherMap API Documentation: https://openweathermap.org/api
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def mood_matches_weather(mood: str, weather: str) -> bool:
    """
    Match mood with weather condition.
    
    """
    mood_weather_map = {
        "happy": "clear",
        "sad": "rain",
        "angry": "storm",
        "calm": "clouds"
    }
    return mood_weather_map.get(mood) == weather


def fetch_song_recommendation(mood: str):
    """
    Fetch a song recommendation based on the user's mood using Last.fm API.
    Last.fm API Documentation: https://www.last.fm/api
    """
    url = f"http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag={mood}&api_key={LASTFM_API_KEY}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        tracks = response.json().get("tracks", {}).get("track", [])
        if tracks:
            return tracks[0].get("name")  # Return the first track name
    return None
