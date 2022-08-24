from aiohttp import web
import asyncio


def index(request):
    return web.Response(body=b"<h1>Hello World!</h1>")


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route("GET", "/index", index)
    server = await loop.create_server(app.make_handler(), "127.0.0.1", 8000)
    return server


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()


if __name__ == "__main__":
    main()
