FROM python:3.10-bullseye

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./src ./src
COPY ./service.py ./service.py

CMD ["python", "service.py"]