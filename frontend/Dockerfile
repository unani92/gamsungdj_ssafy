# FROM node:lts-alpine as build-stage
# WORKDIR /app
# ADD package.json ./
# ADD . ./

# # npm install && npm run build
# RUN npm install
# RUN npm run build

# # production stage -- nginx
# FROM nginx:stable-alpine as production-stage
# COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
# COPY --from=build-stage /app/dist /usr/share/nginx/html

# CMD [ "nginx", "-g", "daemon off;" ]

FROM ubuntu:16.04 as clone-stage
WORKDIR /app
## install all dependancies
RUN sed -i 's/archive.ubuntu.com/kr.archive.ubuntu.com/g' /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get -y install curl gnupg

# node ver 14
RUN curl -sL https://deb.nodesource.com/setup_14.x  | bash -
RUN apt-get -y install nodejs
RUN npm install

# install nginx
RUN apt-get -y install nginx

ADD . ./
RUN npm install
RUN npm rebuild node-sass
RUN npm run build

COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

CMD [ "nginx", "-g", "daemon off;" ]