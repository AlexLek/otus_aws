FROM alpine:3.10.2
MAINTAINER Alexey Lekarev
RUN apk update --no-cache && apk add nginx --no-cache && apk add wget --no-cache && apk add curl --no-cache && apk add openssl --no-cache
RUN mkdir -p /run/nginx/
RUN mkdir -p /var/www/default/
COPY default.conf /etc/nginx/conf.d/
COPY index.html /var/www/default/

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
EXPOSE 80 443
CMD [ "nginx" ]
