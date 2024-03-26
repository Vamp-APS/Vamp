from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

from database.base import Base


class Database:
    # Configure the connection pool
    POOL_SIZE = 5  # Maximum size of the connection pool
    MAX_OVERFLOW = 10  # Maximum number of connections to allow in addition to pool_size
    # Number of seconds after which a connection is invalidated and recycled
    POOL_RECYCLE = 3600

    def __init__(self, db_url):
        self.engine = create_engine(
            db_url,
            poolclass=QueuePool,
            pool_size=self.POOL_SIZE,
            max_overflow=self.MAX_OVERFLOW,
            pool_recycle=self.POOL_RECYCLE,
            echo=True,
        )
        self.Session = sessionmaker(bind=self.engine)

        Base.metadata.create_all(self.engine)

    def get_session(self):
        if self.Session is None:
            raise Exception("Database was not initialized")

        return self.Session
