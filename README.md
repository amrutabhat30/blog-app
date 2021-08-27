# Blog Application

A Django based application to create and publish stories.

## Features

* Create/Edit/Delete stories
* Up/Down vote stories.
* Displays top 5 stories (home page)
* Filter the stories by time (Past 7 hours, 1 day, 7 days) ,where duration is the number of hours.
* Comment on stories
* Archive stories (admin page, Archives stories won’t be shown on the home page)


## Requirements

* Ubuntu 18.04.5 LTS
* Python [3.9.5] (https://www.python.org/downloads/release/python-395/)
* [MySQL server] (https://dev.mysql.com/downloads/mysql/5.7.html?os=src) 
   
   `sudo apt install mysql-client mysql-server libmysqlclient-dev`


## Getting Started

Setup project environment with [venv](https://docs.python.org/3/library/venv.html) 

    $ python3.9 -m venv ./env/

    $ source env/bin/activate


Clone the repository:

    (env) $  git clone git@github.com:amrutabhat30/blog-app.git

    (env) $ cd blog-app


Then install the dependencies:

    (env) $ pip install -r requirements.txt

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.


Once `pip` has finished downloading the dependencies:

    (env)$ cd blog

    (env)$ python manage.py migrate


( Before running the migrations, create MySQL database named 'blog')

    (env)$ python manage.py runserver


And navigate to http://localhost:8000/stories/



