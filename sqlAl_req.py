from sqlalchemy.engine import base
from sqlalchemy import Column, Integer, String, Date, Text, NUMERIC, ForeignKey, MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select, and_
from sqlalchemy.orm import sessionmaker, relationship, mapper
from sqlalchemy.sql.schema import Table
import sqlAl_tablel


engine = create_engine(
    'sqlite:///Sportsqlalchemy.sqlite', echo=True)


Base = declarative_base(engine)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

print('\n----------------------List of competitions------------------------------------------------------\n\t')
ourComp = session.query(sqlAl_tablel.Competition).all()
for i in ourComp:
    print(i)

print('\n----------------------The result of the competition is 10 seconds.-------------------------------\n\t')
ourComp = session.query(sqlAl_tablel.Competition).filter_by(
    world_record=10).all()
for i in ourComp:
    print(i)


print('\n----------------------Summary information on competitions in Moscow.-------------------------------\n\t')
ourSportsman = session.query(
    sqlAl_tablel.ResultCompetition, sqlAl_tablel.Sportsman).filter(sqlAl_tablel.ResultCompetition.sportsman_id == sqlAl_tablel.Sportsman.sportsman_id).all()
for i in ourSportsman:
    print(i)
print('\n----------------------Competitions in which are not the first places.-------------------------------\n\t')
ourSportsman = session.query(
    sqlAl_tablel.ResultCompetition, sqlAl_tablel.Sportsman).filter(sqlAl_tablel.ResultCompetition.sportsman_id == sqlAl_tablel.Sportsman.sportsman_id).filter(sqlAl_tablel.Sportsman.sportsman_rank >= 2).all()
for i in ourSportsman:
    print(i)

print('\n----------------------Сompetitions in which the date is 05-12-2010 or 05-15-2010.-------------------------------\n\t')
ourSportsman = session.query(
    sqlAl_tablel.ResultCompetition, sqlAl_tablel.Competition).filter(sqlAl_tablel.ResultCompetition.competition_id == sqlAl_tablel.Competition.competition_id).filter((sqlAl_tablel.Competition.set_date == '12-05-2010') | (sqlAl_tablel.Competition.set_date == '15-05-2010')).all()
for i in ourSportsman:
    print(i)
print('\n----------------------Sportsman.---------------------------------------------------\n\t')

ourSportsman = session.query(sqlAl_tablel.Sportsman).all()
for i in ourSportsman:
    print(i)

print('\n----------------------Sportsman result is less than 25 seconds.-------------------------------\n\t')

ourSportsman = session.query(sqlAl_tablel.Sportsman).filter(
    sqlAl_tablel.Sportsman.personal_record < 25).all()
for i in ourSportsman:
    print(i)

print('\n----------------------Sportsman born in 1990.----------------------------------------------------\n\t')

ourSportsman = session.query(sqlAl_tablel.Sportsman).filter(
    sqlAl_tablel.Sportsman.year_of_birth == 1990).all()
for i in ourSportsman:
    print(i)

session.close()
