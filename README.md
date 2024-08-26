# FastAPI Serverless

This project is a FastAPI-based application that provides an endpoint to invoke functions dynamically. It includes a sample function to demonstrate how to handle events and context.

## Table of Contents

- [FastAPI Serverless](#fastapi-serverless)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Example](#example)
    - [Sample Function](#sample-function)
      - [`functions/test/test.py`](#functionstesttestpy)

## Installation

1. Clone the repository

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Start the FastAPI server:
    ```sh
    uvicorn main:app --reload
    ```
    ```sh
    python main.py
    ```

2. The server will be running at `http://127.0.0.1:8000`.

## Example

### Sample Function

The sample function is located in `functions/test/handler.py` and `functions/test/test.py`.

#### `functions/test/test.py`


