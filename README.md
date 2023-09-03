# FastAPI Course Creation

This application uses FastAPI to create and manage courses. Here's a brief overview of the main components:

## Main.py
This file contains the FastAPI application and the endpoint definitions. The `/courses` endpoint is used to fetch all courses.

## Database.py
This file sets up the SQLAlchemy engine and sessionmaker. We're using SQLite for our database.

## Models.py
This file contains the SQLAlchemy models for our database. The `Course` model represents a course, with fields for id, name, code, status, description, and instructor_id.

## Running the Application
To run the application, use the command `uvicorn main:app --reload`. This will start the FastAPI server on your local machine.

## Creating a Course
To create a course, make a POST request to the `/courses` endpoint with the following JSON body:

