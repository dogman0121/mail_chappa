FROM python:3.10-slim

COPY . .

RUN pip install -r requirements.txt

EXPOSE 25

CMD ["python", "main.py"]

