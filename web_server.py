from aiohttp import web


async def retrieve_metrics(request):
    data = {"hello": "world"}
    return web.json_response(data)


app = web.Application()
app.router.add_get("/metrics", retrieve_metrics)

if __name__ == "__main__":
    web.run_app(app)
