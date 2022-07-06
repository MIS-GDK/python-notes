# aiohttpdemo_polls/main.py
from aiohttp import web

from settings import config, BASE_DIR
from routes import setup_routes
from db import pg_context
import asyncio
import sys
import aiohttp_jinja2
import jinja2

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = web.Application()
app["config"] = config
# aiohttp_jinja2.setup(
#     app,
#     loader=jinja2.FileSystemLoader(str(BASE_DIR / "aiohttpdemo_polls" / "templates")),
# )
setup_routes(app)
# On startup, the code is run until the yield. When the application is shutdown the code will resume and close the DB connection.
app.cleanup_ctx.append(pg_context)
web.run_app(app)
