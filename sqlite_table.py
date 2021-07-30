import sqlite3

with sqlite3.connect('Sport.sqlite') as conn:
    cursor = conn.cursor()
    try:
        cursor.executescript("""CREATE TABLE sportsman (
  	            sportsman_id integer PRIMARY KEY,
  	            sportsman_name TEXT,
  	            sportsman_rank TEXT,
                year_of_birth INTEGER,
  	            personal_record NUMERIC(100),
  	            country TEXT
              );        
      
        INSERT INTO sportsman VALUES(1, '  Ivanov Ivan   ', '1', 1990, 10, '    Russia   ');
        INSERT INTO sportsman VALUES(2, ' Petrov Nikolay ', '3', 1990, 17, '    Russia   ');
        INSERT INTO sportsman VALUES(3, 'Dmitriev Sergey ', '5', 1991, 20, '    Russia   ');
        INSERT INTO sportsman VALUES(4, '  John Smith    ', '2', 1995, 20, 'Great Britain');
        INSERT INTO sportsman VALUES(5, 'Jackson Michael ', '4', 1990, 18, '      USA    ');
        INSERT INTO sportsman VALUES(6, ' Julio Iglesias ', '6', 1985, 20, '    Spain    ');
         """)

    except sqlite3.Error as e:
        print(e)
        conn.rollback()
    else:
        conn.commit()
    finally:
        print(' GOOD sportsman!!! ')

with sqlite3.connect('Sport.sqlite') as conn:
    cursor = conn.cursor()
    try:
        cursor.executescript("""CREATE TABLE result_competition(
                 res_id int PRIMARY key,
                 competition_id int NOT NULL,
                 sportsman_id int NOT NULL,
                 result_sportsman int NOT NULL check(result_sportsman > 0),
                 city TEXT,
                 hold_date DATE,
                 FOREIGN key(competition_id) REFERENCES competition,
                 FOREIGN key(sportsman_id) REFERENCES sportsman,
                 UNIQUE(competition_id, sportsman_id) );

       
              INSERT INTO result_competition VALUES (1 , 1, 1, 3, 'Moscow', '05-15-2010');
              INSERT INTO result_competition VALUES (2 , 2, 1, 1, 'Moscow', '05-15-2010');
              INSERT INTO result_competition VALUES (3 , 3, 2, 3, 'Moscow', '05-15-2010');
              INSERT INTO result_competition VALUES (4 , 3, 4, 5, 'Moscow', '05-15-2010');
              INSERT INTO result_competition VALUES (5 , 6, 3, 2, 'Moscow', '05-15-2010');
              INSERT INTO result_competition VALUES (6 , 7, 3, 1, 'Moscow', '05-15-2010');
              INSERT INTO result_competition VALUES (7 , 4, 5, 1, 'Moscow', '05-15-2010');
              INSERT INTO result_competition VALUES (8 , 5, 5, 2, 'Moscow', '05-15-2010');
              INSERT INTO result_competition VALUES (9 , 7, 6, 2, 'Moscow', '05-15-2010');
              INSERT INTO result_competition VALUES (10, 8, 6, 1, 'Moscow', '05-15-2010');
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
        conn.rollback()
    else:
        conn.commit()
    finally:
        print(' GOOD result_competition!!! ')


with sqlite3.connect('Sport.sqlite') as conn:
    cursor = conn.cursor()
    try:
        cursor.executescript("""CREATE TABLE competition (
              	competition_id integer PRIMARY key,
              	competition_name TEXT,
              	world_record numeric (100, 0),
              	set_date DATE
              );


            INSERT INTO competition VALUES (1, '  running 100 meters   ', 10, '02-10-2002');
            INSERT INTO competition VALUES (2, '  running 500 meters   ', 30, '02-12-2002');
            INSERT INTO competition VALUES (3, '  running 1000 meters  ', 60, '02-11-2002');
            INSERT INTO competition VALUES (4, '  running 200 meters   ', 15, '05-12-2002');
            INSERT INTO competition VALUES (5, 'ice skating 200 meters ', 10, '12-05-2010');
            INSERT INTO competition VALUES (6, 'ice skating 500 meters ', 10, '12-05-2010');
            INSERT INTO competition VALUES (7, 'ice skating 800 meters ', 25, '15-05-2010');
            INSERT INTO competition VALUES (8, 'ice skating 1000 meters', 40, '15-05-2010');
            INSERT INTO competition VALUES (9, 'ice skating 1200 meters', 50, '15-05-2010');
             
        """)

    except sqlite3.Error as e:
        print(e)
        conn.rollback()
    else:
        conn.commit()
    finally:
        print(' GOOD competition!!! ')
