Project: Ruby's Costa Rica Guide

Link: [http://104.131.176.111/][host]

[host]:http://104.131.176.111/
[github]:https://github.com/silveruby/costa-rica-guide
[server_setup]:https://github.com/silveruby/costa-rica-guide/blob/master/server_setup.md
---

## Introduction

This app was created for Udacity Fullstack Nanodegree project 3. 

The task was to create a catalog web application which handles database CRUD functionalities and user authentication & authorization. 

I used the Flask, Boostrap, SQLAlchemy and Facebook login for this project.  

I was traveling in Costa Rica when working on this project so I got inspired to create a personal Costa Rica Guide to keep track of my travel encounters (i.e. cool plants and favorite fruits)

--- 

## API End points

### A. JSON
	http://104.131.176.111/category/JSON
	http://104.131.176.111/category<category_id>/item/JSON
	http://104.131.176.111/category/<category_id>/item/<item_id>/JSON

### B. XML
	http://104.131.176.111/category/XML
	http://104.131.176.111/category<category_id>/item/XML
	http://104.131.176.111/category/<category_id>/item/<item_id>/XML

---

## CRUD functionalities

The app have CRUD functionalities for Category, Item and Comment. Here are some notes about how they work. 

1. The app can be viewed without login.
2. Users must login to be able to create new comment on Item page
3. Users can edit or delete comments belong to them, but they cannot edit or delete comments belong to other users. 
4. Only authorized users can create, edit and delete Categories and Items. 
5. You can **update the list of authorized users on 'authorized_users.json' file**

---

## How to run application

1. **Source:** Download files from [github repository][github]
2. **Environment:** You'll need to have SQLAlchemy, Flask and oauth2client on your server. In fact, checkout [server_setup.md][server_setup] for detailed instruction on how to setup the server. 
3. **Database:** Database can be set up by running 'python database_setup.py'
4. **Start:** Once you've completed step 1, 2 and 3, then you can run 'python \__init__.py' to start the application
5. **Test:** Open your favorite browser and test the app
