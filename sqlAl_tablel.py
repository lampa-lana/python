from sqlalchemy import create_engine
from sqlalchemy.engine import base
from sqlalchemy import Column, Integer, String, Date, Text, NUMERIC, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine(
    'sqlite:///Sportsqlalchemy.sqlite', echo=True)


Base = declarative_base()


class Sportsman(Base):
    __tablename__ = 'sportsman'
    sportsman_id = Column(Integer, primary_key=True)
    sportsman_name = Column(Text)
    sportsman_rank = Column(Text)
    year_of_birth = Column(Integer)
    personal_record = Column(Integer)
    country = Column(Text)

    def __init__(self, sportsman_id, sportsman_name, sportsman_rank, year_of_birth, personal_record, country):
        self.sportsman_id = sportsman_id
        self.sportsman_name = sportsman_name
        self.sportsman_rank = sportsman_rank
        self.year_of_birth = year_of_birth
        self.personal_record = personal_record
        self.country = country

    def __repr__(self):
        return '\t''Sportsman {}, {} '  '\n'' ''======================================'' '  '\n'' sportsman rank:{}'  '\n'' year of birth:{}'  '\n'' personal record:{} '  '\n'' country:{} '  '\n'' ''======================================'' '  '\n'''.format(self.sportsman_id, self.sportsman_name, self.sportsman_rank, self.year_of_birth, self.personal_record, self.country)


class Competition(Base):
    __tablename__ = 'competition'
    competition_id = Column(Integer, primary_key=True)
    competition_name = Column(Text)
    world_record = Column(Integer)
    set_date = Column(Text)

    def __init__(self, competition_id, competition_name, world_record, set_date):
        self.competition_id = competition_id
        self.competition_name = competition_name
        self.world_record = world_record
        self.set_date = set_date

    def __repr__(self):
        return ' ''=============================================================================='' ''\n'' Competition {}, {}  world record: {} set date:{}' '\n'' ''=============================================================================='' '  '\n'''.format(self.competition_id, self.competition_name, self.world_record, self.set_date)


class ResultCompetition(Base):
    __tablename__ = 'result_competition'
    res_id = Column(Integer, primary_key=True)
    competition_id = Column(Integer, ForeignKey('competition.competition_id'))
    sportsman_id = Column(Integer, ForeignKey('sportsman.sportsman_id'))
    result_sportsman = Column(Integer)
    city = Column(Text)
    hold_date = Column(Text)

    def __init__(self, res_id, competition_id, sportsman_id, result_sportsman, city, hold_date):
        self.res_id = res_id
        self.competition_id = competition_id
        self.sportsman_id = sportsman_id
        self.result_sportsman = result_sportsman
        self.city = city
        self.hold_date = hold_date

    def __repr__(self):
        return '\t''Result of Competition {} ''\n'' Competition number in the competition table: {} '  '\n'' ''======================================'' '  '\n'' sportsman id: {}'  '\n'' result sportsman:{} '  '\n'' city: {}'  '\n'' hold date: {}'  '\n'' ''======================================'' '  '\n'''.format(self.res_id, self.competition_id, self.sportsman_id, self.result_sportsman, self.city, self.hold_date)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
