FROM node:lts-alpine as build-stage
WORKDIR /app
ADD package.json ./
ADD . ./

# npm install && npm run build
RUN npm install
RUN npm run build

# production stage -- nginx
FROM nginx:stable-alpine as production-stage
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf

CMD [ "nginx", "-g", "daemon off;" ]