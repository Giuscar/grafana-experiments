FROM python:3.11

WORKDIR .
RUN pip install aiohttp
RUN pip install pymongo
COPY . .
CMD ["./entrypoint.sh"]
