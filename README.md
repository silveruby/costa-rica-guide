Project: Ruby's Costa Rica Guide

Link: [http://rubyscostaricaguide.heroku.com/](http://rubyscostaricaguide.heroku.com/)

<<<<<<< HEAD
=======

>>>>>>> 2c351f667a6f13d45b3dcb988bea0dce5cb6e980
---

## Introduction

This app was created for Udacity Fullstack Nanodegree project 3. 

The task was to create a catalog web application that handles database CRUD functionalities and provide user authentication & authorization. 

I used the Flask framework, Boostrap, SQLAlchemy and Facebook login for this project.  

<<<<<<< HEAD
Since I am traveling in Costa Rica at the time of making this application, I've designed it as a little online Costa Rica guide to keep track of my travel experiences here. 
=======
I built this site while I was traveling in Costa Rica so I've made it as a little online Costa Rica guide to keep track of my travel experiences. 
>>>>>>> 2c351f667a6f13d45b3dcb988bea0dce5cb6e980

## How to run the application

1. **Source:** Download files from GitHub repository - [https://github.com/silveruby/udacity-full-stack/tree/master/P3](https://github.com/silveruby/udacity-full-stack/tree/master/P3)
2. **Environment:** You'll need to have SQLAlchemy, Flask and oauth2client on your server. In fact, check imports in the start of file project.py for full list. 
3. **Database:** Database is prepopulated by rubyscostarica.db file but if you want to create a new one, run 'python database_setup.py'
4. **Start:** Once you've completed step 1, 2 and 3, then you can run 'python project.py' to start the application
5. **Test:** Open your favorite browser and go to [http://localhost:5000/](http://localhost:5000/) to test app

## CRUD functionalities

The app have CRUD functionalities for Category, Item and Comment. Here are some notes about how they work. 

1. The app can be viewed without login.
2. Users must login to be able to create new comment on Item page
3. Users can edit or delete comments belong to them, but they cannot edit or delete comments belong to other users. 
4. Only authorized users can create, edit and delete Categories and Items. 
5. You can **update the list of authorized users on 'authorized_users.json' file**

<<<<<<< HEAD
## API End points


### A. JSON
	http://localhost:5000/category/JSON
	http://localhost:5000/category<category_id>/item/JSON
	http://localhost:5000/category/<category_id>/item/<item_id>/JSON

### B. XML
	http://localhost:5000/category/XML
	http://localhost:5000/category<category_id>/item/XML
	http://localhost:5000/category/<category_id>/item/<item_id>/XML

=======
>>>>>>> 2c351f667a6f13d45b3dcb988bea0dce5cb6e980


