import psycopg2
import csv

def load_course_database(db_name, csv_filename):
	conn = psycopg2.connect(database = db_name, user = "postgres", host = "/tmp/", password = "cpassword");
	cur = conn.cursor();
	
	with open(csv_filename, 'rU') as csvfile:
		reader = csv.reader(csvfile);
		for row in reader:
			SQL = "INSERT INTO coursedata (deptID, courseNum, semester, meetingType, seatsTaken, seatsOffered, instructor) VALUES (%s, %s, %s, %s, %s, %s, %s);";
			data = ( (row[0],), (int(row[1]),), (int(row[2]),), (row[3],), (int(row[4]),), (int(row[5]),), (row[6],));
			cur.execute(SQL, data);
	conn.commit();
	cur.close();
	conn.close();

if __name__ == "__main__":
	db_name = 'course1';
	csv_filename = 'seas-courses-5years.csv';
	load_course_database(db_name, csv_filename);
