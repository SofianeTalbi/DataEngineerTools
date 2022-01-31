FROM python:3.8

COPY requirements.txt /home/
RUN pip3 install -r /home/requirements.txt

WORKDIR /home
#COPY . .

ENV FLASK_APP=run
ENV FLASK_DEBUG=1
CMD  ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
