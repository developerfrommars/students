FROM python:3.8.1
COPY . /sampleapp
WORKDIR /sampleapp
ENV SQLALCHEMY_DATABASE_URI mysql://root:<db_password>@<db_container_ip>/mysql
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]