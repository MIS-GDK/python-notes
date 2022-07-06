# aiohttpdemo_polls/views.py
from aiohttp import web
import aiohttp_jinja2
import db


# @aiohttp_jinja2.template("index.html")
async def index(request):
    async with request.app["db"].acquire() as conn:
        cursor = await conn.execute(db.question.select())
        records = await cursor.fetchall()
        questions = [dict(q) for q in records]
        # return {"questions": questions}
        return web.Response(body=b"<h1>Index</h1>")
