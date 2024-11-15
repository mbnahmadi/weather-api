
https://roadmap.sh/projects/weather-api-wrapper-service


# Weather API with Django

This project is a Django-based Weather API that fetches weather data from a third-party service (Visual Crossing). It includes features like caching with Redis, rate limiting, and API documentation with Swagger.

## Features
- **City-based Weather Information**: Fetches weather data for a specified city.
- **Latitude and Longitude Support**: Retrieves weather information using geographic coordinates.
- **Caching with Redis**: Optimizes performance by caching responses for 12 hours.
- **Rate Limiting**: Protects the API from abuse by limiting the number of requests per user.
- **Error Handling**: Handles scenarios like invalid inputs and third-party API failures gracefully.
- **API Documentation**: Fully documented using Swagger and ReDoc.

---

## Installation

### Prerequisites
- Python 3.8+
- Django 5.x
- Redis
- Visual Crossing API Key
- Virtual Environment (Recommended)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>


2. **Create a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Set Up Environment Variables**: Create a .env file in the root directory and add the following variables:
   ```bash
   weather_api_key=<Your Visual Crossing API Key>

5. **Start the Server**:
   ```bash
   python manage.py runserver


## API Endpoints   
### 1. City-based Weather API
Endpoint: /api/weather/city/
Method: GET
Query Parameters:
- city (required): Name of the city.
Example Request:
   ```bash
   curl -X GET "http://localhost:8000/api/location-data/?city=London"
   ```


### 2. Lat/Lon-based Weather API
Endpoint: /api/weather/coordinates/
Method: GET
Query Parameters:
latitude (required): Latitude of the location.
longitude (required): Longitude of the location.
Example Request:
   ```bash
   curl -X GET "http://localhost:8000/api/latlon_data/?latitude=35.6892&longitude=51.3890"
   ```

## Rate Limiting
The API applies the following rate limits per user:

10 requests per minute
These limits can be customized in the settings.py file.   


## Documentation
Interactive API documentation is available:

Swagger UI: http://localhost:8000/swagger/
ReDoc: http://localhost:8000/redoc/