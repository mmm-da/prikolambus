FROM node:latest as frontend-build-stage
WORKDIR /frontend
COPY ./anekdot-frontend/package*.json ./
RUN npm install
COPY ./anekdot-frontend/ .
RUN npm run build

FROM nginx:1.19.7-alpine as production-stage
WORKDIR /var/www/app
COPY --from=frontend-build-stage /frontend/dist /var/www/app
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf