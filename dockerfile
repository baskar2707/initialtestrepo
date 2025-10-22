FROM Ubuntu
RUN apt update && apt install apache2 -y && apt clean
COPY index.html /var/www/html/index.html
EXPOSE 80
CMD ["apachectl","-D","FOREGROUND"]
