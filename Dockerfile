FROM python:3.11

WORKDIR .
RUN pip install aiohttp
RUN pip install pymongo
COPY . .
CMD ["python", "./web_server.py"]
