FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV PYTHONUNBUFFERED=1
#CMD ["python", "create_tables.py"]

ENV FLASK_APP=app.py



CMD python create_tables.py && flask run --host=0.0.0.0