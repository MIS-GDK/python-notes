# aiohttpdemo_polls/views.py
from aiohttp import web
import aiohttp_jinja2
import db


async def index(request):
    async with request.app["db"].acquire() as conn:
        cursor = await conn.execute(db.question.select())
        records = await cursor.fetchall()
        questions = [dict(q) for q in records]
        return web.Response(text=str(questions))


# async def index(request):
#     return web.Response(text="Hello Aiohttp!!!")
