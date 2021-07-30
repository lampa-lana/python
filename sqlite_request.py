import sqlite3
import re

with sqlite3.connect('Sport.sqlite') as conn:
    cursor = conn.cursor()

    try:
        print('\n----------------------List of competitions------------------------------------------------------\n\t')
        get_column_names = cursor.execute("select * from competition limit 1")
        col_name = [i[0] for i in get_column_names.description]
        print(col_name)

        cursor.execute("""SELECT * from competition ; """)
        result = cursor.fetchall()

        for i in result:
            print('      ', i[0], '      ', '  ',
                  i[1], '  ',  i[2], '      ', i[3])

        # ---------------------------------------------------------------------------------------------------------------
        print('\n----------------------The result of the competition is 10 seconds.-------------------------------\n\t')

        get_column_names = cursor.execute("select * from competition limit 1")
        col_name = [i[0] for i in get_column_names.description]
        print(col_name)

        cursor.execute(
            """SELECT * from competition where world_record = 10;""")

        result = cursor.fetchall()

        for i in result:
            print('      ', i[0], '      ', '  ',
                  i[1], '   ',  i[2], '      ', i[3])

         # ---------------------------------------------------------------------------------------------------------------
        print('\n----------------------Summary information on competitions in Moscow.-------------------------------\n\t')
        my_list = ['res_id', 'city_name', 'res_sportsman_id',
                   'sportsman_id', 'sportsman_name', ]
        print(my_list)

        res = cursor.execute(
            """SELECT
               result_competition.res_id as res_id, result_competition.city as city_name, result_competition.sportsman_id as res_sportsman_id,
               sportsman.sportsman_id as sportsman_id, sportsman.sportsman_name as sportsman_name
               from result_competition
               left JOIN sportsman on sportsman.sportsman_id=result_competition.sportsman_id
               ;""")

        result = res.fetchall()

        for i in result:
            print('    ', i[0], ' ', '   ',
                  i[1], '            ',  i[2], '             ', i[3], '        ', i[4])

         # ---------------------------------------------------------------------------------------------------------------
        print('\n----------------------Competitions in which are not the first places.-------------------------------\n\t')
        my_list = ['res_id', 'city_name', 'res_sportsman_id',
                   'sportsman_id', 'sportsman_name', 'sportsman_country', 'sportsman_rank']
        print(my_list)
        cursor.execute(
            """SELECT
               result_competition.res_id as res_id, result_competition.city as city_name, result_competition.sportsman_id as res_sportsman_id,
               sportsman.sportsman_id as sportsman_id, sportsman.sportsman_name as sportsman_name,sportsman.country as sportsman_country, sportsman.sportsman_rank as sportsman_rank
               from result_competition
               left JOIN sportsman on sportsman.sportsman_id=result_competition.sportsman_id
               WHERE sportsman.sportsman_rank>'1';""")

        result = cursor.fetchall()

        for i in result:
            print('    ', i[0], ' ', '   ',
                  i[1], '            ',  i[2], '             ', i[3], '        ', i[4], '     ', i[5], '     ', '   ', i[6])

        # ---------------------------------------------------------------------------------------------------------------
        print('\n----------------------Сompetitions in which the date is 05-12-2010 or 05-15-2010.-------------------------------\n\t')
        get_column_names = cursor.execute("select * from competition limit 1")
        col_name = [i[0] for i in get_column_names.description]
        print(col_name)
        cursor.execute(
            """SELECT * from competition WHERE set_date BETWEEN '12-05-2010' and '15-05-2010';""")

        result = cursor.fetchall()

        for i in result:
            print('      ', i[0], '      ', '  ',
                  i[1], ' ',  i[2], '       ', i[3])

         # ---------------------------------------------------------------------------------------------------------------
        print('\n----------------------Sportsman.----------------------------------------------------\n\t')
        get_column_names = cursor.execute("select * from sportsman limit 1")
        col_name = [i[0] for i in get_column_names.description]
        print(col_name)
        cursor.execute(
            """SELECT * from sportsman ;""")

        result = cursor.fetchall()

        for i in result:
            print('      ', i[0], '      ', '  ',
                  i[1], '         ',  i[2], '         ', i[3], '         ', i[4], '         ', i[5])

         # ---------------------------------------------------------------------------------------------------------------
        print('\n----------------------Sportsman result is less than 25 seconds.-------------------------------\n\t')
        get_column_names = cursor.execute("select * from Sportsman limit 1")
        col_name = [i[0] for i in get_column_names.description]
        print(col_name)
        cursor.execute(
            """SELECT * from sportsman where personal_record < 25;""")

        result = cursor.fetchall()

        for i in result:
            print('      ', i[0], '      ', '  ',
                  i[1], '         ',  i[2], '         ', i[3], '         ', i[4], '         ', i[5])

        # ---------------------------------------------------------------------------------------------------------------
        print('\n----------------------Sportsman born in 1990.----------------------------------------------------\n\t')
        get_column_names = cursor.execute("select * from Sportsman limit 1")
        col_name = [i[0] for i in get_column_names.description]
        print(col_name)
        cursor.execute(
            """SELECT * from Sportsman WHERE year_of_birth = 1990;""")

        result = cursor.fetchall()

        for i in result:
            print('      ', i[0], '      ', '  ',
                  i[1], '        ',  i[2], '         ', i[3], '         ', i[4], '         ', i[5])
         # ---------------------------------------------------------------------------------------------------------------
        print('\n----------------------Sportsman born in 1990 by name.----------------------------------------------------\n\t')
        get_column_names = cursor.execute("select * from sportsman limit 1")
        col_name = [i[0] for i in get_column_names.description]
        print(col_name)
        cursor.execute(
            """SELECT sportsman_name, year_of_birth from sportsman WHERE year_of_birth = 1990;""")

        result = cursor.fetchall()

        for i in result:
            print('                   ', i[0],
                  '           ', '         ', i[1])

    except sqlite3.Error as e:
        print(e)
        conn.rollback()
    else:
        conn.commit()
    finally:
        print(' GOOD!!! ')
