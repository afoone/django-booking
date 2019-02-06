FROM python:3.6.4
MAINTAINER Alfonso Tienda "afoone@hotmail.com"

COPY requirements /app/requirements
RUN apt update && apt-get install -y python3-dev libmysqlclient-dev
RUN pip install --upgrade pip
RUN pip install -r /app/requirements/base.txt 

COPY . /app
WORKDIR /app/demo

RUN pip install -e ../
#RUN python manage.py loaddemo

EXPOSE 80
CMD ["python", "manage.py", "runserver", "0:80"]

