# Job Application Tracker

YouTube Presentation Link: Coming soon

## Project Overview

Job Application Tracker is a terminal-based Python program designed to help users organize and manage job applications. The program will allow users to add job applications, view saved applications, update application statuses, search by company name, and count applications by status and exit the program safely.

This project is being developed as part of a Python Project 1 focused on demonstrating competency with the core topics from Python Crash Course Chapters 1 through 7.

## Planned Features

* View all job applications
* Add a new job application
* Update the status of an existing application
* Search applications by company name
* Count applications by status
* Exit the program safely

## Python Concepts Demonstrated

This project demonstrate the following Python concepts:

* Variables and simple data types
* Strings and numbers
* Lists
* Dictionaries
* if, elif, and else statements
* for loops
* while loops
* User input with input()
* Functions 
* Docstrings
* Importingfunctions from another Python file
* Basic terminal interaction (git bash)

## Design Plan

The program uses a list to store multiple job applications. Each job application is stored as a dictionary because every application has several related pieces of information, such as company name, job title, date applied, application status, and notes.

This design makes sense because a user can have many job applications, and each application needs to keep multiple pieces of information together.

## Current Development Status

The main version of the project is complete. The program can view applications, add new applications, update application statuses, search by company name, count applications by status, and exit the program safely. 

Future improvements could include saving applications to a file, making the search case-insensitive, adding input validation, or creating a simple HTML/CSS to display for the applications. 

## How to Run

To run this program, open the project folder in the terminal and type: 
python main.py

```bash
python main.py
```
Then follow the menu options displayed in the terminal. 
## Example Menu
Job Application Tracker
1. View all applications
2. Add a new application
3. Update application status
4. Search by company 
5. Count applications by status
6. Exit 
## Author

Alberto Medina
Youtube Presentation link: https://youtu.be/c4UbIXhTBAI
Slide Deck: [Project 1 Slide Deck](Job_Application_Tracker_Project1_Slides_Requirement_Aligned.pptx)