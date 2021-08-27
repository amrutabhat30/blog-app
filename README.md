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


## Screenshots

Create a story

![create_story](https://user-images.githubusercontent.com/17699193/131182084-7dd49f82-589a-4206-a1a7-cef8a0be6bdd.png)


Validating input fields

![url_validation](https://user-images.githubusercontent.com/17699193/131182108-c14dda82-fc18-4baf-9b69-724fd7458bdd.png)


Home Page displaying recent stories. Here you can edit/delete/upvote/downvote a story

![home+page_down_vote](https://user-images.githubusercontent.com/17699193/131182124-f54b65bc-4798-457c-849c-843fd426a0d4.png)


Post comments on a story

![story_comment](https://user-images.githubusercontent.com/17699193/131182133-5bca6ea7-c7ed-4664-b8fd-8ca2adaaf4b3.png)


Admin page to archive a story that won't be shown on the home page

![archive_story2](https://user-images.githubusercontent.com/17699193/131182179-ed073c0b-979b-4dc3-adcd-ed0c4f298e14.png)


Filter the stories by time (Past 7 hours, 1 day, 7 days)

![time_filter](https://user-images.githubusercontent.com/17699193/131182190-122b53e1-450f-450e-9b83-08cffb5b3ca5.png)



