from sqlalchemy import create_engine
from sqlalchemy.engine import base
from sqlalchemy import Column, Integer, String, Date, Text, NUMERIC, func, and_, or_, not_, aliased, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlAl_tablel


engine = create_engine(
    'sqlite:///Sportsqlalchemy.sqlite', echo=True)


Base = declarative_base()
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
# ourSportsman = session.query(
#     sqlAl_tablel.ResultCompetition).filter().all()
# for i in ourSportsman:
#     print(i)
print('\n----------------------Competitions in which are not the first places.-------------------------------\n\t')


print('\n----------------------Сompetitions in which the date is 05-12-2010 or 05-15-2010.-------------------------------\n\t')
ourComp = session.query(sqlAl_tablel.Competition).filter_by(
    set_date='12-05-2010 and 15-05-2010').all()
for i in ourComp:
    print(i)


# ourResult = session.query(sqlAl_tablel.ResultCompetition).all()
# for i in ourResult:
#     print(i)

# session.close()
