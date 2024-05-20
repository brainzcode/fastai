# Branding and Blog Generation API

This project provides a FastAPI-based web application for generating branding snippets, keywords, and blog content. It offers various endpoints to help create content ideas and details based on provided prompts and topics.

## Features

- Generate branding snippets based on a given prompt.
- Generate keywords for branding based on a given prompt.
- Generate blog topic ideas tailored to a specific audience and keywords.
- Generate blog section titles based on a given topic, audience, and keywords.
- Generate detailed content for a specific blog section.
- Cross-Origin Resource Sharing (CORS) is enabled for all origins.

## Endpoints

### Root Endpoint
- **GET /**

  Returns a simple greeting message.

  ```json
  {
    "Hello": "World"
  }
  ```

### Generate Branding Snippet
- **GET /generate_snippet/{prompt}/**

  Generates a branding snippet for the given prompt.

  **Parameters:**
  - `prompt` (str): The input prompt for generating the snippet.

  **Response:**
  ```json
  {
    "snippet": "Generated branding snippet",
    "keywords": []
  }
  ```

### Generate Branding Keywords
- **GET /generate_keywords/{prompt}/**

  Generates branding keywords for the given prompt.

  **Parameters:**
  - `prompt` (str): The input prompt for generating keywords.

  **Response:**
  ```json
  {
    "snippet": null,
    "keywords": ["keyword1", "keyword2"]
  }
  ```

### Generate Blog Topic Ideas
- **GET /generate_blog/{topic}/{audience}/{keywords}/**

  Generates blog topic ideas based on the topic, audience, and keywords.

  **Parameters:**
  - `topic` (str): The main topic for the blog.
  - `audience` (str): The target audience for the blog.
  - `keywords` (str): Keywords to be included in the blog.

  **Response:**
  ```json
  {
    "snippet": "Generated blog topic ideas"
  }
  ```

### Generate Blog Section Titles
- **GET /generate_blog_titles/{topic}/{audience}/{keywords}/**

  Generates blog section titles based on the topic, audience, and keywords.

  **Parameters:**
  - `topic` (str): The main topic for the blog.
  - `audience` (str): The target audience for the blog.
  - `keywords` (str): Keywords to be included in the blog.

  **Response:**
  ```json
  {
    "snippet": "Generated blog section titles"
  }
  ```

### Generate Blog Section Details
- **GET /generate_blog_section/{topic}/{section}/{audience}/{keywords}/**

  Generates detailed content for a specific blog section.

  **Parameters:**
  - `topic` (str): The main topic for the blog.
  - `section` (str): The section topic for the blog.
  - `audience` (str): The target audience for the blog.
  - `keywords` (str): Keywords to be included in the blog section.

  **Response:**
  ```json
  {
    "snippet": "Generated blog section details"
  }
  ```

### Generate Branding Snippet and Keywords
- **GET /generate_snippet_and_keywords/{prompt}/**

  Generates both a branding snippet and keywords for the given prompt.

  **Parameters:**
  - `prompt` (str): The input prompt for generating the snippet and keywords.

  **Response:**
  ```json
  {
    "snippet": "Generated branding snippet",
    "keywords": ["keyword1", "keyword2"]
  }
  ```

## Input Validation

- The input prompt length is validated to be under 32 characters. If the input exceeds this length, a `400 Bad Request` error is returned.

## Running the Application

To run the application, execute the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

## Deployment

This application is compatible with AWS Lambda using the Mangum adapter. 

## License

This project is licensed under the MIT License.

## Acknowledgements

Special thanks to the developers of FastAPI, Mangum, and all other open-source projects that contributed to this application.
