# AI-Handwriting-Scribe

A robust, containerized machine learning pipeline for handwriting synthesis. This project integrates end-to-end experiment tracking, model registry, and containerized deployment for seamless inference.

## Key Features

* **Handwriting Synthesis**: Generates realistic handwriting based on specified text and style IDs.
* **Dockerized Deployment**: Fully containerized environment ensuring consistent performance across different environments.
* **MLflow Integration**: Automated experiment tracking and model registry for experiment reproducibility and lifecycle management.
* **API-First Design**: FastAPI-based interface providing an interactive Swagger UI for testing and integration.

## Technical Stack

* **ML Framework**: TensorFlow 1.x Compatibility Mode
* **API / Serving**: FastAPI and Uvicorn
* **Containerization**: Docker
* **Tracking / Registry**: MLflow

## Quick Start

### 1. Prerequisites

Ensure you have the following installed on your machine:

* [Docker](https://www.docker.com/)
* [Git](https://git-scm.com/)

### 2. Clone the Repository

```bash
git clone https://github.com/Who-Moiz/AI-Handwriting-Scribe.git
cd AI-Handwriting-Scribe
```

### 3. Build the Docker Image

```bash
docker build -t ai-scribe-app .
```

### 4. Run the Application

```bash
docker run -p 8000:8000 ai-scribe-app
```

### 5. Access the API

After running the container, open your browser and visit:

```text
http://localhost:8000/docs
```

You can test handwriting generation through the interactive Swagger UI.

## MLflow Tracking

This project uses MLflow to log inference parameters, performance metrics, and model information.

To view experiment history and registered models locally, run:

```bash
mlflow ui
```

Then open your browser and visit:

```text
http://127.0.0.1:5000
```

## Project Structure

```text
AI-Handwriting-Scribe/
│
├── server.py              # Main FastAPI application logic
├── Dockerfile             # Docker configuration for containerizing the application
├── requirements.txt       # Python dependencies
├── mlflow/                # MLflow experiment data and model registry
├── *.py                   # Supporting modules for RNN cells and handwriting synthesis
└── README.md              # Project documentation
```

## API Usage

Once the application is running, the FastAPI Swagger UI allows you to test the available endpoints directly.

Typical workflow:

1. Open the API documentation at `http://localhost:8000/docs`.
2. Select the handwriting generation endpoint.
3. Provide the required input text and style ID.
4. Execute the request.
5. View or download the generated handwriting output.

## Docker Commands

### Build Image

```bash
docker build -t ai-scribe-app .
```

### Run Container

```bash
docker run -p 8000:8000 ai-scribe-app
```

### Stop Running Container

First, check the running containers:

```bash
docker ps
```

Then stop the container:

```bash
docker stop <container_id>
```

## Requirements

The main dependencies are listed in `requirements.txt`.

Core dependencies include:

* TensorFlow
* FastAPI
* Uvicorn
* MLflow
* NumPy
* Matplotlib

To install dependencies manually without Docker, run:

```bash
pip install -r requirements.txt
```

## Purpose of the Project

The purpose of AI-Handwriting-Scribe is to provide a complete machine learning workflow for handwriting synthesis. It combines model inference, API deployment, Docker-based environment management, and MLflow experiment tracking into one professional pipeline.

This makes the project suitable for:

* Machine learning deployment practice
* Handwriting generation experiments
* API-based model serving
* MLOps learning and demonstration
* Containerized AI application development

## Author

**Abdul Moiz**

GitHub: [Who-Moiz](https://github.com/Who-Moiz)
