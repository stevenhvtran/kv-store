FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app.py ./

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]

