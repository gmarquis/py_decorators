README.md

py_decorators >> main.py <br />
requirements.txt <br />

Dockerfile = <br />
FROM python:3.7-alpine <br />
WORKDIR /service <br />
COPY requirements.txt . <br />
RUN apk add curl <br />
RUN pip install -r requirements.txt <br />
COPY . ./ <br />
EXPOSE 5000 <br />
ENTRYPOINT ["python", "main.py"] <br />

docker build -t simple_decorators -f Dockerfile . <br />
docker run -it simple_decorators <br />
