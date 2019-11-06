# This script defines the sQLLite database, tables and schema
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

# Define the address table
Base = declarative_base()
class Address(Base):
    __tablename__ = 'gAddress' # geocoded addresses

    # define columns
    id = Column(Integer, primary_key=True)
    search_string = Column(String(100), nullable=False)
    lat = Column(Float, nullable=True)
    lon = Column(Float, nullable=True)
    search_time = Column(String(50))

    @property
    def serialize(self):
        return {'id': self.id,
                'search_string': self.search_string,
                'lat': self.lat,
                'lon': self.lon,
                'search_time':self.search_time}

# create this new db and write the schema and tables.
engine = create_engine('sqlite:///addresses.db')
Base.metadata.create_all(engine)