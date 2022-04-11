FROM python:3.7-bullseye
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
