
FROM python:3.8-slim-buster

WORKDIR /app


COPY . .

RUN pip install --upgrade pip
RUN pip uninstall opencv-python
RUN pip uninstall opencv-contrib-python
RUN pip uninstall opencv-contrib-python-headless

RUN apt-get update -y && \
    apt-get install build-essential cmake pkg-config -y
    
RUN pip install -r requirements.txt

CMD ["python", "main.py"]