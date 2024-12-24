FROM python:latest

RUN mkdir "mail_chappa"

WORKDIR "mail_chappa"

COPY . "mail_chappa"

RUN pip install -r requirements.txt

CMD ["python", "main.py"]

