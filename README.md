# Backend Application

## Introduction

This repository contains the backend code for our application, which was implemented using FastAPI.

## Prerequisites

Ensure you have the following installed on your machine:
- Python 3.8+
- `uv` package manager

## Setup Instructions

Go to the Backend Directory before proceeding

### Step 1: Install `uv`

Install the `uv` package manager using the command below:
```sh
pip install uv
```

### Step 2: Install Dependencies

Navigate to the root directory of the backend repository and run the following command to install all the dependencies:
```sh
uv venv
source .venv/bin/activate
uv pip install
uv add fastapi
```

### Step 3: Run the FastAPI Application

Start the FastAPI server using the command below:
```sh
fastapi dev
```

The application will be accessible at `http://127.0.0.1:8000`.
To view the documentation of the API, visit `http://127.0.0.1:8000/docs` and ensure the API server is running.

## Additional Information

### Test Implementation

There is a `DocEmbedding.ipynb` file in this repository that contains some implementation logic that has not yet been integrated into the API. You can review and run the notebook to understand and test the logic.
