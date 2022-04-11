FROM FROM --platform=linux/amd64 python:3.7-alpine
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
