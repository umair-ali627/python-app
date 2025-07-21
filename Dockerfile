FROM python:3.7

WORKDIR /app

COPY . /usr/share/nginx/html

EXPOSE 8888

CMD ["node", "app.js"]
