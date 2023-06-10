# Menggunakan base image Python
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Copy kode aplikasi Flask
COPY . .

# Set environment variable PORT
ENV PORT 8080

# Menjalankan aplikasi Flask
CMD ["python", "app.py"]
