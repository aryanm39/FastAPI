## CORS (Cross-Origin Resource Sharing)

### Addressing "Failed to Fetch" Errors and CORS Issues

**Error:**  
This error occurs when the front end (running on `localhost:3000`) tries to access the 
back end (running on `localhost:8000`).  
Browsers block cross-origin requests by default for security reasons.

- **allow_origins**: A list of origins that are allowed to make requests.  
  Set it to `["http://localhost:3000"]` to allow requests from your React development server.


## Connecting FastAPI to PostgreSQL 
1. Create db.py: This file handles the database connection.
2. Import Dependencies:
3. Define Database URL:
4. Create Engine:
5. Create Local Session:
6. Define Base:
7. get_db Function:
8. create_table Function

## Defining Database Models
1. Create models.py: This file defines the database tables.
2. Import Dependencies:
3. Define the Student Class:

## Defining Schemas with Pydantic
1. Create schemas.py: This file defines the data structures for request and response bodies.
2. Import Dependencies:
3. Define Student:
4. Define StudentCreate:

## Defining Services
1. Create services.py: This file contains functions for database interactions.
2. Import Dependencies:
3. create_student Function:
4. get_students Function:
5. get_student Function:
6. update_student Function:
7. delete_student Function:

## Creating the FastAPI Application
1. Create main.py: This file defines the API endpoints.
2. Import Dependencies:
3. Create FastAPI Instance:
4. Define Endpoints:

GET /students (Retrieve all students):  \
POST /students (Create a new student):  \
GET /students/{id} (Retrieve a specific student): \
PUT /students/{id} (Update a specific student): \
DELETE /students/{id} (Delete a specific student):  
