FROM python:3.8

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

RUN groupadd -g 10001 freetak && \
   useradd -u 10000 -g freetak freetak \
   && chown -R freetak:freetak /app

USER freetak:freetak

WORKDIR /app/FreeTAKServer-UI

# Web UI Port
EXPOSE 5000

ENTRYPOINT [ "python", "run.py"]