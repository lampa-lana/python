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

sportsman1 = sqlAl_tablel.Sportsman(1, 'Ivanov Ivan', '1', 1990, 10, 'Russia')
sportsman2 = sqlAl_tablel.Sportsman(
    2, 'Petrov Nikolay', '3', 1990, 17, 'Russia')
sportsman3 = sqlAl_tablel.Sportsman(
    3, 'Dmitriev Sergey', '5', 1991, 20, 'Russia')
sportsman4 = sqlAl_tablel.Sportsman(
    4, 'John Smith', '2', 1995, 20, 'Great Britain')
sportsman5 = sqlAl_tablel.Sportsman(5, 'Jackson Michael', '4', 1990, 18, 'USA')
sportsman6 = sqlAl_tablel.Sportsman(
    6, 'Julio Iglesias', '6', 1985, 20, 'Spain')
session.add(sportsman1)
session.add(sportsman2)
session.add(sportsman3)
session.add(sportsman4)
session.add(sportsman5)
session.add(sportsman6)


competition1 = sqlAl_tablel.Competition(
    1, 'Running 100 meters', 10, '02.11.2002')
competition2 = sqlAl_tablel.Competition(
    2, 'Running 500 meters', 30, '02.12.2002')
competition3 = sqlAl_tablel.Competition(
    3, 'Running 1000 meters', 60, '02-11-2002')
competition4 = sqlAl_tablel.Competition(
    4, 'Running 200 meters', 15, '05-12-2002')
competition5 = sqlAl_tablel.Competition(
    5, 'Ice skating 200 meters', 10, '12-05-2010')
competition6 = sqlAl_tablel.Competition(
    6, 'Ice skating 500 meters', 10, '12-05-2010')
competition7 = sqlAl_tablel.Competition(
    7, 'Ice skating 800 meters', 25, '15-05-2010')
competition8 = sqlAl_tablel.Competition(
    8, 'Ice skating 1000 meters', 40, '15-05-2010')
competition9 = sqlAl_tablel.Competition(
    9, 'Ice skating 1200 meters', 50, '15-05-2010')
session.add(competition1)
session.add(competition2)
session.add(competition3)
session.add(competition4)
session.add(competition5)
session.add(competition6)
session.add(competition7)
session.add(competition8)
session.add(competition9)

result1 = sqlAl_tablel.ResultCompetition(1, 1, 1, 3, 'Moscow', '05-15-2010')
result2 = sqlAl_tablel.ResultCompetition(2, 2, 1, 1, 'Moscow', '05-15-2010')
result3 = sqlAl_tablel.ResultCompetition(3, 3, 2, 3, 'Moscow', '05-15-2010')
result4 = sqlAl_tablel.ResultCompetition(4, 3, 4, 5, 'Moscow', '05-15-2010')
result5 = sqlAl_tablel.ResultCompetition(5, 6, 3, 2, 'Moscow', '05-15-2010')
result6 = sqlAl_tablel.ResultCompetition(6, 7, 3, 1, 'Moscow', '05-15-2010')
result7 = sqlAl_tablel.ResultCompetition(7, 4, 5, 1, 'Moscow', '05-15-2010')
result8 = sqlAl_tablel.ResultCompetition(8, 5, 5, 2, 'Moscow', '05-15-2010')
result9 = sqlAl_tablel.ResultCompetition(9, 7, 6, 2, 'Moscow', '05-15-2010')
result10 = sqlAl_tablel.ResultCompetition(10, 8, 6, 1, 'Moscow', '05-15-2010')
session.add(result1)
session.add(result2)
session.add(result3)
session.add(result4)
session.add(result5)
session.add(result6)
session.add(result7)
session.add(result8)
session.add(result9)
session.add(result10)


session.commit()
