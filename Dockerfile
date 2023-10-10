# Use an official pypy runtime as a parent image
FROM pypy:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Define the command to run your Python application
CMD ["pypy3", "bookstore.py"]
