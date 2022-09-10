FROM Python:3.7.9

WORKDIR /Fast-Api

COPY ./requirements.txt /Fast-Api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Fast-Api/requirements.txt

COPY ./sql_app /Fast-Api/sql_app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]