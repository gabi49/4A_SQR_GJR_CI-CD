FROM python:3.8

RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip install flask

COPY . .

ENV FLASK_APP=projet.py
ENV FLASK_DEBUG=True

EXPOSE 5000

CMD ["export", "FLASK_APP=projet.py"]
CMD ["flask", "run"]
