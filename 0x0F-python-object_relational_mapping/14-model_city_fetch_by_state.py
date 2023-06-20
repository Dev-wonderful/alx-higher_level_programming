#!/usr/bin/python3
"""To fetch all cities by state"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]
    ), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(City, State)\
        .filter(City.state_id == State.id).order_by(City.id)

    for city, state in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
