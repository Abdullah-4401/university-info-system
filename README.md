
# University Data Manager

This project is a Django REST framework application for managing university data and handling user authentication. It includes functionalities for fetching, storing, updating, and deleting university data from an external API, as well as user registration, login, logout, and password reset functionalities.

## Features

- **User Authentication**: Register, login, logout, and reset password functionalities.
- **University Data Management**: Fetch, store, list, update, and delete university data from an external API.

## Requirements

- Python 3.x
- Django 3.x or higher
- Django REST Framework
- Requests library

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/university-data-manager.git
    cd university-data-manager
    ```

2. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Run migrations:**

    ```sh
    python manage.py migrate
    ```

4. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

5. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

## Usage

### Authentication Endpoints

- **Register**: `POST /auth/register/`
- **Login**: `POST /auth/login/`
- **Logout**: `POST /auth/logout/`
- **Forgot Password**: `POST /auth/forgot-password/`
- **Get CSRF Token**: `GET /auth/get-csrf-token/`

### University Data Endpoints

- **Fetch Data**: `GET /university/fetch/` (Allows unauthenticated access)
- **Fetch and Store Data**: `POST /university/fetch-and-store/` (Requires authentication)
- **List Universities**: `GET /university/` (Requires authentication)
- **Retrieve University**: `GET /university/<id>/` (Requires authentication)
- **Update University**: `PUT /university/<id>/` (Requires authentication)
- **Partial Update University**: `PATCH /university/<id>/` (Requires authentication)
- **Delete University**: `DELETE /university/<id>/` (Requires authentication)

## Views and Handlers

### Views

- **FetchUniversityDataView**: Handles fetching data from the external API without storing it.
- **FetchAndStoreUniversityDataView**: Handles fetching data from the external API and storing it in the database.
- **UniversityListView**: Lists all university data stored in the database.
- **UniversityDetailView**: Retrieves, updates, partially updates, or deletes a specific university data by its ID.

### Handlers

The data fetching and storing logic is encapsulated in the `UniversityDataHandler` class in `app/university/utils.py`:


