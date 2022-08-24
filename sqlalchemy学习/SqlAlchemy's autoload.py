from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker


class User_account(object):
    pass


# ----------------------------------------------------------------------
def loadSession():
    """"""
    dbPath = "hrhnprod:Ww7v*SLuhrDJ@HRHNDB_CS"
    engine = create_engine("oracle://%s" % dbPath, echo=True)

    metadata = MetaData(engine)
    user_account = Table("user_account", metadata, autoload=True)
    mapper(User_account, user_account)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session


if __name__ == "__main__":
    session = loadSession()
    res = session.query(User_account).all()
    for i in res:
        print(i.id, i.name, i.fullname)
    session.close()
