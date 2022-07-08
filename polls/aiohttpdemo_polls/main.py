from aiohttp import web
from routes import setup_routes
from settings import config
from db import pg_context
import asyncio
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
app = web.Application()
setup_routes(app)
app["config"] = config
app.cleanup_ctx.append(pg_context)
web.run_app(app, host="localhost", port=8080)
