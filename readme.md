# Mood-Weather-Song Recommendation API

This API recommends a song based on the user's mood and the current weather in their city. It uses the OpenWeatherMap API to fetch weather data and the Last.fm API to fetch song recommendations.

---

## Features
- Accepts **mood** and **city** as input.
- Fetches current weather data for the given city using the OpenWeatherMap API.
- Matches the user's mood with the current weather condition.
- Recommends a song based on the user's mood using the Last.fm API.

---

## Prerequisites
- Python 3.7 or higher installed on your system.
- API keys for:
  - [OpenWeatherMap](https://openweathermap.org/api)
  - [Last.fm](https://www.last.fm/api)

---

## Setup Instructions

### main.py 
`main.py` is the main file of the application. It contains the core logic for fetching weather data, matching it with the user's mood, and recommending a song. Ensure this file is executed to start the API.

---

## 1. Install Dependencies
Install the required Python packages:
```powershell
pip install -r requirements.txt
```

### 2. API Key Configuration
The API keys for OpenWeatherMap and Last.fm are already hardcoded in the `main.py` file for simplicity. No additional configuration is required.

### 3. Run the Application
Start the application by running:

```powershell
python main.py
```

### 3.1 Run with Uvicorn (Optional)
To run the application with Uvicorn for better performance and development features, use the following command:

```powershell
uvicorn main:app --reload
```

### 4. Testing the API

You can test the API using Postman. A Postman collection has been created to simplify testing.

### Postman Collection
Use the following link to access the Postman collection:
[Postman Collection Link](https://sravan-9900507.postman.co/workspace/Sravan's-Workspace~cb55a45c-4d37-4a9d-860e-9d7d6b9b071e/request/43722260-22470c78-6e86-4e1a-b66e-d6c6b28474bb?action=share&creator=43722260&ctx=documentation)

### Steps to Test
1. Import the Postman collection using the link above.
2. Use the `GET /recommendation/` endpoint with the following query parameters:
   - `mood`: The user's mood (e.g., `happy`, `sad`).
   - `city`: The name of the city (e.g., `London`).
3. Example Request:

---

### Note for Project
For this project, the API keys are hardcoded directly into the application for simplicity.
