FROM python:3
RUN pip install Django==4.0.6
COPY . .
RUN python manage.py migrate
CMD ["python","manage.py","runserver","0.0.0.0:8001"]

