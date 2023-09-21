# 
FROM python:3.10

# 
WORKDIR /code

# Install libraries
RUN pip install -U pip setuptools wheel 
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN python -m spacy download en_core_web_lg

# 
COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8999"]
