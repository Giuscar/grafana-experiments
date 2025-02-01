FROM python:3.11

WORKDIR .
RUN pip install aiohttp
COPY . .
CMD ["python", "./web_server.py"]
