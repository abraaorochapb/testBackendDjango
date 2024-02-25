# Backend Test

This project was built with Python, DRF(Django) and OpenAPI for documentation

## Running the project

Follow the next steps to run the project on your local machine:

1. **Clone the project:**

    ```bash
    git clone https://github.com/abraaorochapb/testBackendDjango
    ```

2. **Database config:**

    - Open the file `settings.py` inside `testBackendDjango`.
    - Insert your local database credentials.

3. **Run the Migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Start the server:**

    ```bash
    python manage.py runserver
    ```

You can access the server via url `http://localhost:8000/`.

You can find documentation about the endpoints on `http://localhost:8000/api/docs/`