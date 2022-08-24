from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.dialects.oracle import NUMBER, VARCHAR2
from sqlalchemy import select
from sqlalchemy.orm import Session

metadata_obj = MetaData()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", NUMBER(10), primary_key=True),
    Column("name", VARCHAR2(30)),
    Column("fullname", VARCHAR2(100)),
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", NUMBER(10), primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", VARCHAR2(200), nullable=False),
)
# print(user_table.c.keys())
# print(user_table.primary_key)
engine = create_engine("oracle://hrhnprod:Ww7v*SLuhrDJ@HRHNDB_CS", echo=True)
# metadata_obj.create_all(engine)
stmt = select(user_table).where(user_table.c.name == "sandy")
print(stmt)
with engine.connect() as conn:
    result = conn.execute(stmt)
    for i in result:
        print(i)

with Session(engine) as sess:
    for res in sess.execute(stmt):
        print(res)
print(select(user_table.c.name, user_table.c.fullname))
