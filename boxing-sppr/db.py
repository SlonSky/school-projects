from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, create_session, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:////home/slonsky/dev/mine/boxing_sppr/boxing.db', echo=True)
Session = scoped_session(sessionmaker(bind=engine))

class Boxer(Base):
    __tablename__ = 'boxers'

    id = Column(Integer, primary_key=True)

    name = Column(String)

    age = Column(Integer)

    won = Column(Integer)
    drawn = Column(Integer)
    lost = Column(Integer)
    kos = Column(Integer)

    country = Column(String)

    experience = Column(Integer)


class Referee(Base):
    __tablename__ = 'referees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)


class Place(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)


def init_db():
    Base.metadata.create_all(engine)


class DBManager:

    @staticmethod
    def start():
        init_db()
        Session()

    @staticmethod
    def exit():
        Session.remove()


    def find_all_places(self):
        return Session.query(Place).all()

    def update_place(self, id, place):
        self._update(id, place, Place, ['name' , 'country'])

    def find_place(self, id):
        return self._find_by_id(Place, id)

    def add_place(self, place):
        Session.add(place)
        Session.commit()

    def delete_place(self, id):
        place = self._find_by_id(Place, id)
        if place is not  None:
            Session.delete(place)
            Session.commit()

    def find_all_boxers(self):
        return Session.query(Boxer).all()


    def add_boxer(self, boxer):
        Session.add(boxer)
        Session.commit()

    def _update(self, id, entity, table, fields):
        found = self._find_by_id(table, id)
        if found is not None:
            for i in fields:
                setattr(found, i, getattr(entity, i))

            Session.add(found)
            Session.commit()

    def update_boxer(self, id, boxer):
        self._update(id, boxer, Boxer, ['name', 'age', 'won', 'lost', 'drawn', 'kos', 'country', 'experience'])

    def find_boxer(self, id):
        return self._find_by_id(Boxer, id)

    def delete_boxer(self, id):
        boxer = self._find_by_id(Boxer, id)
        if boxer is not None:
            Session.delete(boxer)
            Session.commit()

    def _find_by_id(self, table, id):
        return Session.query(table).filter(table.id == id).first()

###########################

    def find_all_referees(self):
        return Session.query(Referee).all()

    def delete_referee(self, id):
        referee = self._find_by_id(Referee, id)
        Session.delete(referee)
        Session.commit()

    def add_referee(self, referee):
        Session.add(referee)
        Session.commit()

    def update_referee(self, id, referee):
        self._update(id, referee, Referee, ['name', 'country'])

    def find_referee(self, id):
        return Session.query(Referee).filter(Referee.id == id).first()

