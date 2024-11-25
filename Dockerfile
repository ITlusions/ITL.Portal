FROM ghcr.io/astral-sh/uv:python3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN uv pip install --no-cache-dir -r /tmp/requirements.txt --system

# Copy the entire application code into the container
COPY ./src /app

# Expose port 80 to allow traffic
EXPOSE 80

CMD ["gunicorn", "-b", "0.0.0.0:80", "--access-logfile", "-", "--forwarded-allow-ips", "*","main:app"]