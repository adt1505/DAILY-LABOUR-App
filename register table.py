import sqlite3
conn=sqlite3.connect('DL.db')
print("Opened database successfully");

conn.execute('''CREATE TABLE register
         (Username  VARCHAR    NOT NULL,
          email     VARCHAR     NOT NULL,
          phno      INT     NOT NULL,
          gender    CHAR     NOT NULL,
          password  VARCHAR   NOT NULL,
          conpsd    VARCHAR    NOT NULL);
         ''')
print ("Table created successfully");
conn.close()
