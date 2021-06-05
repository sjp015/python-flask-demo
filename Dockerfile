FROM python:3

WORKDIR .

COPY requirements.txt .
COPY app.py .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python","./app.py"]
