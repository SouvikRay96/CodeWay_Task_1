# CodeWay_Task_1
A To-Do-List Application

A To-Do List application is an useful application that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing users
to create, update, and track their to-do lists.

All the users in this To-Do-List Application have to register their account with this Application.

Then after Successfull registration an unique User-Id will be generated which the users have to remember for Logging in into the Application from the next time.

For each users a seperate table will be maintained which will contain their tasks list along with the Start and End Time Provided by the user.

The Users can view their Task List, Create/Insert new Task into the Task List and Update the Task List to Specify whether the task is completed or not.

This application is built by integrating Python with the Database MySQL for storing the records and TaskList of the Users.

The Application has two files 
    1) main.py
        In the main.py file , the main application will be running which will be just communicate with the User.
    2) databaseConnectionModule.py
        In the databaseConnectionModule.py , the Database operations are performed which will communicate between the Database and the Python main.py file.
        