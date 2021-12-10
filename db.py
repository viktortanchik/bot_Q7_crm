import sqlite3

#con = sqlite3.connect('sqlite_python.db')
con = sqlite3.connect('bot.sqlite')


def crate_db():
    try:
        sqlite_connection = sqlite3.connect('bot.sqlite')
        cursor = sqlite_connection.cursor()
        sqlite_create_table_query = ("""CREATE TABLE IF NOT EXISTS users(
                   uid INTEGER PRIMARY KEY AUTOINCREMENT,
                   chat TEXT ,
                   user_id TEXT ,
                   username TEXT ,
                   real_name TEXT ,
                   name_of_agency TEXT ,
                   payid TEXT ,
                   strikes TEXT ,
                   hyperlink TEXT ,
                   tag TEXT ,
                   comments TEXT 
                   );
                """)

        print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()

        # cursor = sqlite_connection.cursor()
        # sqlite_create_table_query = ("""CREATE TABLE IF NOT EXISTS channel(
        #                    uid INTEGER PRIMARY KEY AUTOINCREMENT,
        #                    chat_name_telegram TEXT ,
        #                    chat_name_slack TEXT
        #                    );
        #                 """)
        #
        # print("База данных подключена к SQLite")
        # cursor.execute(sqlite_create_table_query)
        # sqlite_connection.commit()
        # print("Таблица SQLite создана")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def sql_insert_one(con, entitie):
    cursorObj = con.cursor()
    cursorObj.execute(
    'INSERT INTO users(chat_name) VALUES(?)', entitie)
    con.commit()

def get_all(con):
    cursorObj = con.cursor()
    all =cursorObj.execute("SELECT * FROM users")
    alls=[]
    for row in all:
        alls.append(row)
        #print(row)    #con.execute("SELECT * FROM users")
    return alls


#sql_insert_one(con,'1')
def sql_insert_all(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO users (chat,user_id,username,real_name,name_of_agency,payid,strikes,hyperlink,tag,comments) VALUES(? ,? ,?, ?, ?,?,?,?,?,?)', entities)
    con.commit()


def sql_channel_name(con,name):
    cursorObj = con.cursor()
    stre = ''.join(name)
    query = "SELECT slack_channel_name FROM settings WHERE telegram_group_name = " + "'" + str(stre) + "'"  # +str(name)
    print(query)
    cursorObj.execute(query)
    values = cursorObj.fetchone()
    print(values)
    return values[0]


#print(get_all(con))
#rows = get_all(con)
# mes = ''
# for row in rows:
#     # print(row)
#     mes + str(row)
#     mes += '\n'
#     print(mes)

#print(sql_channel_name(con,'test_chat'))
#crate_db()
#test= ['Chat_name','ID1312312','USER_fdsfsdf','id_name_sdrwserwe','test','Chat_name','ID1312312','USER_fdsfsdf','id_name_sdrwserwe','test']
#sql_insert_all(con,test)
#crate_db()

