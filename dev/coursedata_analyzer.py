import psycopg2
import csv

db_name = 'course1';
csv_filename = 'seas-courses-5years.csv';

conn = psycopg2.connect(database = db_name, user = "postgres", host = "/tmp/", password = "cpassword");
cur = conn.cursor();

cur.execute("""SELECT instructor from coursedata""");
rows = cur.fetchall();
for row in rows:
	print(" ", row[0]);
