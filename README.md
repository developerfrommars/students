to run:

1. docker run --name <name> -e MYSQL_ROOT_PASSWORD=<db_password> --network=<network_name> -p 3306:3306 -d mysql:5.7

2. edit dockerfile

3. login to your db and run query.sql

4. docker run -d -p 5000:5000 --name <name> --network=<network_name> <image_name>
