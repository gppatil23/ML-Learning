FROM python:3.15.0b4-slim-trixie
WORKDIR /code
ENV FLASK_ENV=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000 
CMD [ "flask","run" ]
