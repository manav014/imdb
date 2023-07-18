FROM node:18-alpine
ARG MY_NAME
ENV MY_NAME=$MY_NAME
EXPOSE 1337
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN env
