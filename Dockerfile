FROM python:3.10

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8000 8001

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
