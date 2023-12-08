import psycopg2 # pip install psycopg2

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
    password = "9999' OR '1' = '1"
    query = "SELECT * FROM public.tbl_user WHERE use_pass = '" + password + "'"

    cursor.execute(query);
    rows = cursor.fetchall();
    for row in rows:
      print(row);
  except:
    print("query exception")


except(Exception, psycopg2.Error) as error:
  print("error connecting", error)
