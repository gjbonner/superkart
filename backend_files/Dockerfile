FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "app:app"]
