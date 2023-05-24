FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

COPY .aptible.yml /.aptible/.aptible.yml

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
