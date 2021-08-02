import datetime
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine import base
from sqlalchemy import Column, Integer, String, DateTime, Date, Text, NUMERIC, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine(
    'sqlite:///Sportsqlalchemy.sqlite', echo=True)


Base=declarative_base()


class Competition(Base):
    __tablename__='competition'
    competition_id=Column(Integer, primary_key=True)
    competition_name=Column(Text)
    world_record=Column(Integer)
    set_date=Column(Text)

    def __init__(self, competition_id, competition_name, world_record, set_date):
        self.competition_id=competition_id
        self.competition_name=competition_name
        self.world_record=world_record
        self.set_date=set_date

    def __repr__(self):
        return '\t''Competition {}, {} '  '\n'' ''======================================'' '  '\n'' world record: {}'  '\n'' set date:{}'  '\n''  ''======================================'' '  '\n'''.format(self.competition_id, self.competition_name, self.world_record, self.set_date)
    # def __repr__(self):
    #     return '{}, {}  {} {}'.format(self.competition_id, self.competition_name, self.world_record, self.set_date)


Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
session=Session()

competition1=Competition(1, 'Running 100 meters', 10, '02.11.2002')
competition2=Competition(2, 'Running 500 meters', 30, '02.12.2002')
competition3=Competition(3, 'Running 1000 meters', 60, '02-11-2002')
competition4=Competition(4, 'Running 200 meters', 15, '05-12-2002')
competition5=Competition(5, 'Ice skating 200 meters', 10, '12-05-2010')
competition6=Competition(6, 'Ice skating 500 meters', 10, '12-05-2010')
competition7=Competition(7, 'Ice skating 800 meters', 25, '15-05-2010')
competition8=Competition(8, 'Ice skating 1000 meters', 40, '15-05-2010')
competition9=Competition(9, 'Ice skating 1200 meters', 50, '15-05-2010')
session.add(competition1)
session.add(competition2)
session.add(competition3)
session.add(competition4)
session.add(competition5)
session.add(competition6)
session.add(competition7)
session.add(competition8)
session.add(competition9)
session.commit()

ourSportsman=session.query(Competition).filter_by(
    competition_id=1).all()
for i in ourSportsman:
    print(i)

ourSportsman=session.query(Competition).all()
for i in ourSportsman:
    print(i)


session.close()
