FROM python:3.7-slim

COPY . /app

WORKDIR /app

RUN apt update && \
    apt install gcc -y && \
    pip install dep/pyrqlite && \
    pip install dep/sqlalchemy-rqlite && \
    pip install -r requirements.txt && \
    apt remove gcc -y

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
