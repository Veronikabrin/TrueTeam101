FROM python:3.5-alpine3.11
WORKDIR /opt/app
COPY . /opt/app
RUN pip3 install -r env_requirements.txt
ENTRYPOINT PYTHONPATH="${PYTHONPATH}:./model" python3 app.py