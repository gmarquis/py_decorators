FROM python:3.7-alpine
WORKDIR /service
COPY requirements.txt .
RUN apk add curl
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 5000
ENTRYPOINT ["python", "main.py"]
