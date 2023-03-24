# todo_app

This is a Django ToDo project that uses the PostgreSQL database to store and process data.

## Requirements

- Python 3.8 or higher
- Django 3.2 or higher
- PostgreSQL 13 or higher
- Psycopg2 2.9 or higher

## Installation

1. Clone the repository using the command `git clone https://github.com/username/projectname.git`
2. Go to the project folder using the command `cd projectname`
3. Create and activate a virtual environment using the commands `python -m venv venv` and `source venv/bin/activate`
4. Install the required dependencies using the command `pip install -r requirements.txt`
5. Set up the PostgreSQL database using the commands `psql -U postgres -c "CREATE DATABASE dbname"` and `psql -U postgres -c "CREATE USER username WITH PASSWORD 'password'"`
6. Apply migrations to the database using the command `python manage.py migrate`
7. Run the development server using the command `python manage.py runserver`
