from aiohttp import web
from routes import setup_routes, setup_static_routes
from settings import config, BASE_DIR
from db import pg_context
import asyncio
import sys
import aiohttp_jinja2
import jinja2
from middlewares import setup_middlewares

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
app = web.Application()
setup_routes(app)
setup_middlewares(app)
# load the config into the application
app["config"] = config
# aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader("aiohttpdemo_polls", "templates"))
aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader(str(BASE_DIR / "aiohttpdemo_polls" / "templates")),
)
app.cleanup_ctx.append(pg_context)
web.run_app(app, host="localhost", port=8080)
