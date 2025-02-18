FROM python:3.9

WORKDIR /app

# Ensure the path is correct
COPY requirements.txt /app/requirements.txt  
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "consumer.py"]
