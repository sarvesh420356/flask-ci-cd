# Use Python 3.12 as the base image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port (Flask default: 5000)
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
