import sqlalchemy as sa
from sqlalchemy import orm

from pypi_org.data.modelbase import SqlAlchemyBase

factory = None


def global_init(db_file: str):
    # Global indica a python que accedemos a la variable global
    global factory

    if factory:
        return
    if not db_file or not db_file.strip():
        raise Exception("You must spcify a db file.")
    conn_str = 'sqlite:///' + db_file.strip()
    print("Connecting to DB with {}".format(conn_str))

    engine = sa.create_engine(conn_str, echo=False)
    factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import pypi_org.data.__all_models 
    SqlAlchemyBase.metadata.create_all(engine)
