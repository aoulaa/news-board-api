# news-board-api

To run without docker
Clone repo

Install dependencies from *requirements.txt* file:

    pip install -r requirements.txt

copy .env.example to .env

Command to create database application migrations:

    python manage.py makemigrations
    python manage.py migrate


Run this command to run the application:

    python manage.py runserver

To run job once a day uncomment this line ('0 0 * * *', 'blog.utils.delete')
 in settings 

run this command to add all defined jobs:

    python manage.py crontab add 

show current active jobs of this project:

    python manage.py crontab show

removing all defined jobs is straight forward:

    python manage.py crontab remove

API requests.
not finished yet.
https://www.postman.com/telecoms-architect-21949474/workspace/news-borad-api
