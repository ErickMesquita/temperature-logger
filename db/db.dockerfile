FROM postgres:latest
LABEL author="Erick Brunoro"

EXPOSE 5432

RUN localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8
ENV LANG pt_BR.utf8

COPY ./init-scripts/ /docker-entrypoint-initdb.d/
RUN ["chmod", "755", "/docker-entrypoint-initdb.d", "-R"]