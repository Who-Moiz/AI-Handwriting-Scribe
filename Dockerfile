# Step 1: Use an official lightweight Python runtime as a parent image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file into the container
COPY requirements.txt .

# Step 4: Install the dependencies inside the container
# We use --no-cache-dir to keep the image size small
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy all project files into the container
COPY . .

# Step 6: Expose the port that FastAPI runs on
EXPOSE 8000

# Step 7: Run the FastAPI server when the container starts
CMD ["python", "server.py"]