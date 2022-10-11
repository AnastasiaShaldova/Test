FROM python:3.8
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN python -m venv venv
RUN cd venv/bin/activate
RUN pip install -r ./requirements.txt

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3114"]