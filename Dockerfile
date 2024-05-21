FROM python:3.8-slim-buster 
#954503069243.dkr.ecr.us-west-2.amazonaws.com/genai-python-base-image:latest
RUN apt-get update && apt-get install -y telnet dnsutils iputils-ping --no-install-recommends && rm -rf /var/lib/apt/lists/*
COPY app1 /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["src/app.py"]



##
