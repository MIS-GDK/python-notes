from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# engine = create_engine(
#     "postgresql://aiohttpdemo_user:aiohttpdemo_pass@127.0.0.1:5432/aiohttpdemo_polls",
#     echo=True,
# )
# with engine.connect() as conn:
#     conn.execute(
#         text("insert into some_table (x,y) values (:x,:y)"),
#         [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
#     )
#     conn.commit()

# engine = create_engine("oracle+cx_oracle://hrhnprod:Ww7v*SLuhrDJ@HRHNDB_CS", echo=True)
# with engine.connect() as conn:
#     conn.execute(text("create table some_table(x int,y int)"))
#     conn.execute(
#         text("insert into some_table (x,y) values (:x,:y)"),
#         [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
#     )
# conn.commit()

# with Session(engine) as session:
#     session.execute(
#         text("UPDATE some_table SET y=:y WHERE x=:x"),
#         [{"x": 1, "y": 10}, {"x": 13, "y": 15}],
#     )
#     session.commit()
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column, ForeignKey, select
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)
    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"))
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


sandy = User(id=2, name="sandy", fullname="Sandy Cheeks")
print(sandy)
engine = create_engine("oracle://hrhnprod:Ww7v*SLuhrDJ@192.168.0.190:1525/HRHNDB")
# session = sessionmaker(bind=engine)
# sess = session()
# sess.add(sandy)
# sess.commit()

stmt = select(User).where(User.name == "sandy")
print(stmt)
with Session(engine) as session:
    for row in session.execute(stmt):
        print(row)
    res = session.execute(
        select(User.name, Address).where(User.id == Address.user_id)
    ).all()
    print(res)
# row = session.execute(select(User)).first()
# print(row)

# user = session.scalars(select(User)).first()
# print(user)

# print(select(User.name, User.fullname))
