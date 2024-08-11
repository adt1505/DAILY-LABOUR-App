import sqlite3
conn = sqlite3.connect('DL.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE login
         (Username      VARCHAR    NOT NULL,
         Password       VARCHAR     NOT NULL);
         ''')
print ("Table created successfully");
conn.close()
