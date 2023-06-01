from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


engine = create_engine('postgresql://gnelkixh:R4HlZoWv-egk4ImngVku0RhYq3uSwPZG@snuffleupagus.db.elephantsql.com/gnelkixh')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()