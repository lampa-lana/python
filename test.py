import sqlite3

# conn = sqlite3.connect('Chinook_Sqlite.sqlite')

# cursor = conn.cursor()

# # cursor.execute('INSERT into artists values(555, "Sergey");')
# # cursor.execute('INSERT into artists values(556, "Sergey1");')
# # cursor.execute('INSERT into artists values(557, "Sergey2");')
# # cursor.execute('INSERT into artists values(558, "Sergey3");')

# # cursor.executescript("""

# #       INSERT into artists values(556, "Sergey2");
# #       INSERT into artists values(557, "Sergey3");
# #       INSERT into artists values(558, "Sergey4");
# # """)


# # people = {
# #     555: 'Mike',
# #     556: 'Alex',
# #     557: 'Peter',
# #     558: 'Mike1',
# # }

# # for i, j in people.item():
# #     cursor.execute(' INSERT into artists values(?, ?);', (i, j))


# # for i, j in people.items():
# #     cursor.execute(' INSERT into artists values (:pk, :Name);',
# #                    {'pk': i+10, 'Name': j})

# # people2 = [
# #     (600, 1),
# #     (601, 2),
# #     (602, 3),
# #     (603, 4),
# # ]

# # cursor.executemany(' INSERT into artists values (?, ?);', people2)

# # cursor.execute('SELECT *  from artists where artistid  > 555;')
# # result = cursor.fetchall()

# # for i in result:
# #     print(i)

# conn.commit()
# # cursor.execute('''
# #     SELECT *
# #     from artists
# #     order by artistid
# #     limit 5;''')

# # my_list = list(cursor)
# # for i in my_list:
# #     print(i)
# cursor.execute('SELECT *  from artists where artistid  > 555;')
# result = cursor.fetchall()

# for i in result:
#     print(i)

# # result = cursor.fetchone()
# # print(result)

# # result = cursor.fetchall()
# # print(result)

# conn.close()

# with sqlite3.connect('Chinook_Sqlite.sqlite') as conn:
#     cursor = conn.cursor()

#     try:
#         cursor.execute('SELECT *  from artists where artistid  > 500;')
#         result = cursor.fetchall()

#         for i in result:
#             print(i)
#     except sqlite3.Error as e:
#         print(e)
#         conn.rollback()
#     else:
#         conn.commit()
#     finally:
#         print(' GOOD!!! ')


with sqlite3.connect('Sport.sqlite') as conn:
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * from competition;')
        result = cursor.fetchall()

        for i in result:
            print(i)
    except sqlite3.Error as e:
        print(e)
        conn.rollback()
    else:
        conn.commit()
    finally:
        print(' GOOD!!! ')
