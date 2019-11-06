# Script for database operations

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from address_db_model import Base, Address
from datetime import datetime
import pytz
from pytz import timezone

# engine = create_engine('sqlite:///addresses.db')
# Base.metadata.bind = engine
# DBsession = sessionmaker(bind=engine)
# session = DBsession()


def get_pst_time():
    # get current time
    date_format = '%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now(tz=pytz.utc)
    date2 = date.astimezone(timezone('US/Pacific'))
    return date2.strftime(date_format)


def create_address(session, search_string, lat, lon):
    address = Address(search_string=search_string, lat=lat, lon=lon,
                      search_time=get_pst_time())
    session.add(address)
    session.commit()


def update_address(session, address_id, search_string=None, lat=None, lon=None):
    # get the row to be edited
    address = session.query(Address).filter_by(id=address_id).one()
    if address:
        if search_string:
            address.search_string = search_string
        if lat:
            address.lat = lat
        if lon:
            address.lon = lon
        address.search_time = get_pst_time()

        # make edits
        session.add(address)
        session.commit()


def delete_address(session, address_id):
    address = session.query(Address).filter_by(id=address_id).one()
    if address:
        session.delete(address)
        session.commit()


def read_address(session, address_id):
    address = session.query(Address).filter_by(id=address_id).one()
    if address:
        return address.serialize


def read_all_addresses(session):
    addresses = session.query(Address).all()
    address_list = [a.serialize for a in addresses]
    return address_list