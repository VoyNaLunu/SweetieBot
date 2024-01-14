from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()


class Watchlist(Base):
    __tablename__ = "watchlists"

    pk = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, name: str, description: str = "") -> None:
        self.name = name
        self.description = description

    def __repr__(self):
        return f"{self.id} {self.name}"


engine = create_engine("sqlite:///botdb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

watchlist = Watchlist(name="test")
session.add(watchlist)
session.commit()
