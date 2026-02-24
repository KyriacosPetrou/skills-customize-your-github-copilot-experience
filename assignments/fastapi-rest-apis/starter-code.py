"""
FastAPI REST API Starter Code
Building REST APIs with FastAPI Framework

TODO: Complete the tasks outlined in the README.md file
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI()

# TODO: Define a Book model using Pydantic
# The model should have: id (int), title (str), author (str), year (int)


# Sample data - using a list to store books
books = []


# TODO: Task 1 - Create a GET endpoint at "/" that returns a welcome message
# The response should be a JSON object with a message


# TODO: Task 2 - GET endpoint at "/books" to return all books


# TODO: Task 2 - GET endpoint at "/books/{book_id}" to return a single book


# TODO: Task 2 - POST endpoint at "/books" to add a new book


# TODO: Task 3 - GET endpoint at "/books/search" with query parameters for filtering


# TODO: Task 4 - DELETE endpoint at "/books/{book_id}" to remove a book


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
