FROM python:3.10.10

WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY tf_serving_exporter.py /app/tf_serving_exporter.py

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

ENTRYPOINT ["python", "tf_serving_exporter.py"]
