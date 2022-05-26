# URL SHORTENER

## Requirements
- Python 3.10
- Django 3.2
- Django REST Framework 3.13

## Available Endpoints

| Endpoint | HTTP Method | Request Body |Result
| --- | --- | --- | --- |
| api | GET | - | Get all shortened urls |
| api | POST | {" full_url" : "your_url_to_shorten "} | Create new short url |
| api/:short_code | GET | - | Get reverse short url | 
