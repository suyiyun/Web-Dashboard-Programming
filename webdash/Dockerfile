FROM python 3.9.2

ADD requirements.txt / requirements.txt

ADD main.py /main.py

ADD Dockerfile /Dockerfile

RUN pip install -r requirements.txt

EXPOSE 8080

COPY ./app /app

CMD ["python3", "main.py"]
