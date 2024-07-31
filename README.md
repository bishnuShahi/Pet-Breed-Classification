# UPDATED VERSION OF PAWFINDER

1. Updated UI to be more user-friendly and easy to use.
2. Optimized the website speed by removing useless and redundant code and updating the existing features to be more straight-forward.
3. Added modularity by saperating ML model into a different API which can be accessed through my github repository "Dog-Breed-API".

## Requirements
- Python 3.11 or higher
- Django 5.0.7
- django-browser-reload 1.13.0
- django-tailwind 3.8.0

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/bishnuShahi/Pet-Breed-Classification.git
    cd Pet-Breed-Classification
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin:
    ```bash
    python manage.py createsuperuser
    ```


## Usage

1. Start the development server:
    ```bash
    python manage.py runserver
    ```
2. Start tailwind:
    ```bash
    python manage.py tailwind start
    ```

3. Open your browser and go to `http://127.0.0.1:8000/` to see the project running.

4. Access the Django admin at `http://127.0.0.1:8000/admin/`.


## Additional Note:
(It hasn't been deployed because to make use of its main feature "Breed Classification" we need to deploy the API too which I couldn't due to some limitations on "Free-Tier" on deployment service providers although I reduced its size by applying some logic myself rather than using heavy libraries but still too big.)
