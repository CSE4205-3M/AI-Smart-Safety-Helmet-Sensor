import psycopg2

conn_string = "dbname = '3M-BE' user='postgres' host='165.246.44.237' password='7381' port='8080'"

conn=psycopg2.connect(conn_string)

cur = conn.cursor()

cur.execute("SELECT * from worker;")

result_all = cur.fetchall()

print(result_all)
conn.commit()

