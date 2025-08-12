# Fitness Assistant

A comprehensive fitness management application built with Django REST Framework that helps users track their fitness journey, create workout plans, manage diet, and earn rewards.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)

## Overview

Fitness Assistant is a web-based application designed to help users manage their fitness journey. It provides features for tracking workouts, creating personalized fitness plans, managing diet through food items and recipes, and earning rewards through achievements and badges.

The application is built using Django and Django REST Framework, providing a robust API for frontend applications to interact with.

## Features

- **User Management**: Create and manage user accounts with authentication
- **Customer Profiles**: Manage customer profiles with details like age, height, weight, and gender
- **Exercise Library**: Browse a collection of exercises with descriptions and difficulty levels
- **Workout Plans**: Create personalized workout plans based on fitness objectives
- **Daily Plans**: Track daily workout plans and mark them as completed
- **Food and Recipe Database**: Access a database of food items and recipes with nutritional information
- **Rewards System**: Earn points, achievements, and badges for completing workouts
- **Filtering**: Filter resources by various parameters like objective type, difficulty level, etc.

## Installation

### Prerequisites

- Python 3.13+
- MySQL database
- Pipenv (for dependency management)

### Steps

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fitnessAssistant.git
   cd fitnessAssistant
   ```

2. Install dependencies using Pipenv:
   ```
   pipenv install
   ```

3. Activate the virtual environment:
   ```
   pipenv shell
   ```

4. Set up the database:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Configuration

The application uses a MySQL database by default. You can configure the database settings in `Fitness_Assistant/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fitness_assistant2',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## API Documentation

### Base URL

All API endpoints are prefixed with `/api/`.

### Authentication

The application provides a custom authentication endpoint:

- **POST /api/authenticate/**: Authenticate a user with username, email, and password

Example request:
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepassword"
}
```

Example response:
```json
{
  "id": 1,
  "username": "johndoe",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com"
}
```

### Customers

- **GET /api/customers/**: List all customers
- **GET /api/customers/{id}/**: Retrieve a specific customer
- **POST /api/customers/**: Create a new customer
- **PATCH /api/customers/{id}/**: Update a customer

#### Filtering

- **GET /api/customers/?gender=M**: Filter customers by gender
- **GET /api/customers/?kind=VG**: Filter customers by kind (vegetarian/non-vegetarian)
- **GET /api/customers/?user__id=1**: Filter customers by user ID

### Exercises

- **GET /api/exercises/**: List all exercises
- **GET /api/exercises/{id}/**: Retrieve a specific exercise

#### Filtering

- **GET /api/exercises/?toughness_level=H**: Filter exercises by toughness level (H, M, E)
- **GET /api/exercises/?objective=WL**: Filter exercises by objective type (WL, BB, FG)

### Jobs

- **GET /api/jobs/**: List all jobs
- **GET /api/jobs/{id}/**: Retrieve a specific job
- **POST /api/jobs/**: Create a new job
- **DELETE /api/jobs/{id}/**: Delete a job

#### Ordering

- **GET /api/jobs/?ordering=completed_at**: Order jobs by completion time

### Plans

- **GET /api/plans/**: List all plans
- **GET /api/plans/{id}/**: Retrieve a specific plan
- **POST /api/plans/**: Create a new plan
- **PATCH /api/plans/{id}/**: Update a plan

#### Filtering

- **GET /api/plans/?customer=1**: Filter plans by customer ID
- **GET /api/plans/?objective_type=WL**: Filter plans by objective type (WL, BB, FG)

### Daily Plans

- **GET /api/daily-plans/**: List all daily plans
- **GET /api/daily-plans/{id}/**: Retrieve a specific daily plan
- **POST /api/daily-plans/**: Create a new daily plan
- **PATCH /api/daily-plans/{id}/**: Update a daily plan

#### Filtering

- **GET /api/daily-plans/?plan=1**: Filter daily plans by plan ID
- **GET /api/daily-plans/?completion_status=true**: Filter daily plans by completion status

### Food Items

- **GET /api/food-items/**: List all food items
- **GET /api/food-items/{id}/**: Retrieve a specific food item

#### Filtering

- **GET /api/food-items/?objective_type=WL**: Filter food items by objective type (WL, BB, FG)
- **GET /api/food-items/?kind=VG**: Filter food items by kind (VG, NVG)

### Recipes

- **GET /api/recipes/**: List all recipes
- **GET /api/recipes/{id}/**: Retrieve a specific recipe

#### Filtering

- **GET /api/recipes/?objective_type=WL**: Filter recipes by objective type (WL, BB, FG)
- **GET /api/recipes/?kind=VG**: Filter recipes by kind (VG, NVG)

### Badges

- **GET /api/badges/**: List all badges
- **GET /api/badges/{id}/**: Retrieve a specific badge
- **POST /api/badges/**: Create a new badge
- **PATCH /api/badges/{id}/**: Update a badge

### Achievements

- **GET /api/achievements/**: List all achievements
- **GET /api/achievements/{id}/**: Retrieve a specific achievement
- **POST /api/achievements/**: Create a new achievement
- **PATCH /api/achievements/{id}/**: Update an achievement

## Usage Examples

### Creating a User and Customer

```python
import requests

# Base URL
base_url = "http://localhost:8000/api"

# Create a customer with a user
response = requests.post(f"{base_url}/customers/", json={
    "user": {
        "username": "johndoe",
        "email": "john@example.com",
        "first_name": "John",
        "last_name": "Doe"
    },
    "age": 30,
    "height": 180.5,
    "weight": 75.0,
    "gender": "M",
    "kind": "NVG"
})

print(response.json())
```

### Authenticating a User

```python
import requests

# Base URL
base_url = "http://localhost:8000/api"

# Authenticate a user
response = requests.post(f"{base_url}/authenticate/", json={
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword"
})

print(response.json())
```

### Creating a Fitness Plan

```python
import requests

# Base URL
base_url = "http://localhost:8000/api"

# Create a fitness plan
response = requests.post(f"{base_url}/plans/", json={
    "objectiveType": "WL",
    "customer": 1,
    "duration_in_days": 14
})

print(response.json())
```

### Marking a Daily Plan as Completed

```python
import requests

# Base URL
base_url = "http://localhost:8000/api"

# Mark a daily plan as completed
response = requests.patch(f"{base_url}/daily-plans/1/", json={
    "completion_status": True
})

print(response.json())
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
