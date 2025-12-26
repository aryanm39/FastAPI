# FastAPI

## Addressing "Failed to Fetch" Errors and CORS Issues

### CORS (Cross-Origin Resource Sharing)

**Error:**  
This error occurs when the front end (running on `localhost:3000`) tries to access the 
back end (running on `localhost:8000`).  
Browsers block cross-origin requests by default for security reasons.

- **allow_origins**: A list of origins that are allowed to make requests.  
  Set it to `["http://localhost:3000"]` to allow requests from your React development server.
