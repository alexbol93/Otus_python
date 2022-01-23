# docker build -t homework03 .
# docker run --rm -p 8000:8000 --name fastapi homework03
FROM python:3.9-buster

WORKDIR /var/app
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.app:app", "--host=0.0.0.0", "--port=8000"]

EXPOSE 8000