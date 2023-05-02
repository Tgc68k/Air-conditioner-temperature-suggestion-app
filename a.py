import sqlite3

from datetime import datetime, timedelta


def app_data(num):
  global now_date
  global thr_day
  conn = sqlite3.connect('./db.sqlite3')
  c = conn.cursor()
  a = 'SELECT time FROM app_data'
  z = str(datetime.now() - timedelta(days=30))
  b = " where time >= '"
  string = a + str(num) + b + z + "'"
  string2 = "select name from sqlite_master where type='table'"
  print(string)
  
  
  c.execute(string)
  result = c.fetchall()
  print(result)
  c.close()
  conn.close()
app_data(3105)
