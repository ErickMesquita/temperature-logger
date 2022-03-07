FROM mysql:latest
LABEL author="Erick Brunoro"

# COPY ./init-scripts/ /docker-entrypoint-initdb.d/
# RUN ["chmod", "755", "/docker-entrypoint-initdb.d", "-R"]
# COPY ./mysql-root.txt /run/secrets/mysql-root.txt
# ENV MYSQL_ROOT_PASSWORD=senha+super+secreta

# ENV MYSQL_DATABASE=Medidas MYSQL_USER=app

# COPY ./mysql-app.txt /run/secrets/mysql-app.txt
# ENV MYSQL_PASSWORD=senha+super+secreta2

# COPY init.sql /usr/src

# RUN ["mysql", "-u $MYSQL_USER", "-p ${cat ${MYSQL_PASSWORD_FILE}}", " < /usr/src/init.sql"]

EXPOSE 3306