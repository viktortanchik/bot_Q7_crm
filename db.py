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
                   comments TEXT, 
                   deposit TEXT
                   );
                """)

        print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
#crate_db()

# Обновления любого значения
def sql_update(con,set,set_name,where,where_name):
    cursorObj = con.cursor()
    strs = 'UPDATE users SET '+str(set)+' = '+"'"+str(set_name)+"'"+' where '+str(where)  +' = '+ "'" +str(where_name)+ "'"
    #'UPDATE users SET original_channel_name = "Rogers" where UID = 2'
    print(strs)
    cursorObj.execute(strs)
    con.commit()

# set = ("user_id")
# set_name = ('TEST_UPDATE')
# where = ('username')
# where_name =('stasgrin01')
# sql_update(con,set,set_name,where,where_name)

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
    cursorObj.execute('INSERT INTO users (chat,user_id,username,real_name,name_of_agency,payid,strikes,hyperlink,tag,comments,deposit) VALUES(? ,? ,?, ?, ?,?,?,?,?,?,?)', entities)
    con.commit()

test=['chat','user_id','username','real_name','name_of_agency','payid','strikes','hyperlink','tag','comments','deposit']

#sql_insert_all(con,test)
def sql_select_original_channel_name(con,id):
    cursorObj = con.cursor()
    stre = ''.join(str(id))
    query = "SELECT * FROM users WHERE uid = " + "'" + str(stre) + "'"  # +str(name)
    #print(query)
    cursorObj.execute(query)
    values = cursorObj.fetchone()
    #print(values)
    return values

#sql_channel_name(con,ues)
def sql_select_id(con,name):
    cursorObj = con.cursor()
    stre =''.join(name)
    query="SELECT * FROM users WHERE username = "+ "'" +str(stre) + "'"  # +str(name)
    #print(query)
    cursorObj.execute(query)
    values = cursorObj.fetchone()
    user = sql_select_original_channel_name(con,values[0])
    return user

