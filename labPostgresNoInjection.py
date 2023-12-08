# pip install psycopg2

import psycopg2

try:
  connection = psycopg2.connect(
    host = "localhost",
    port = "85",
    database = "postgres",
    user = "postgres",
    password = "password"
  )

  print("connected")

  cursor = connection.cursor()

  try:
    user = "Sergio"
    password = "1234"
    query = "SELECT * FROM public.tbl_user WHERE use_name = %s AND use_pass = %s"

    params = (user, password,)

    cursor.execute(query, params);
    rows = cursor.fetchall();
    for row in rows:
      print(row);
  except:
    print("query exception")


except(Exception, psycopg2.Error) as error:
  print("error connecting", error)
