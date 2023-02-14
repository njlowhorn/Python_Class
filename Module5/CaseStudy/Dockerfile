FROM python:3

WORKDIR /opt/data

COPY data.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./data.py"]