# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework, including designing endpoints, handling HTTP methods, defining data models with Pydantic, and implementing request validation.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI application with a simple endpoint that returns a welcome message. This task establishes the foundation for building REST APIs with FastAPI.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Define a GET endpoint at the root path (`/`) that returns a welcome message
- The endpoint should return a JSON response with a message like: `{"message": "Welcome to the Book Store API"}`
- Run the application using uvicorn on port 8000

### 🛠️ Build a Book Store API with Multiple Endpoints

#### Description
Extend the basic application to create a book store API with endpoints for retrieving, adding, and managing books. Use a list to store book data.

#### Requirements
Completed program should:

- Define a Pydantic model called `Book` with fields: `id` (integer), `title` (string), `author` (string), and `year` (integer)
- Implement a GET endpoint at `/books` that returns a list of all books
- Implement a GET endpoint at `/books/{book_id}` that returns a single book by ID
- Implement a POST endpoint at `/books` that accepts a book object and adds it to the list
- Include proper HTTP status codes (200 for success, 404 for not found)
- Example request body for POST:
  ```json
  {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year": 1960
  }
  ```

### 🛠️ Add Query Parameters and Data Validation

#### Description
Enhance the API with query parameters for filtering books and implement automatic request validation using Pydantic models.

#### Requirements
Completed program should:

- Add a GET endpoint at `/books/search` that accepts query parameters: `author` (string) and `year` (integer, optional) to filter books
- Validate that the `year` parameter is a valid 4-digit integer
- Return filtered results based on the query parameters
- Handle invalid requests gracefully with appropriate error messages
- Example: `/books/search?author=Harper%20Lee&year=1960` should return books by Harper Lee published in 1960

### 🛠️ Implement DELETE Endpoint

#### Description
Add functionality to delete books from the store using a DELETE endpoint.

#### Requirements
Completed program should:

- Implement a DELETE endpoint at `/books/{book_id}` that removes a book by ID
- Return a confirmation message when a book is successfully deleted
- Return a 404 error if the book ID does not exist
- Example response on success: `{"message": "Book deleted successfully"}`
