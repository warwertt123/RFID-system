import sqlite3

conn=sqlite3.connect('RFID.db')
cursor=conn.cursor()

#cursor.execute("DELETE FROM in_out_time")

#cursor.execute("DROP TABLE in_out_time")

#cursor.execute('CREATE TABLE in_out_time  (NO TEXT , INOUTtime TEXT) ')

#cursor.execute("INSERT INTO in_out_time  (NO, INOUTtime)  VALUES('mike','LABCDE')")

#cursor.execute("DELETE  FROM PEOPLE_DATA WHERE NO='{0}'".format('ADDDDDDDDDDD'))                   

conn.commit()
conn.close()

