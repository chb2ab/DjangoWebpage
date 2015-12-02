import psycopg2

global conn
conn = psycopg2.connect("postgres://hvcaoxvgdsxzui:ZnOM8mecGoc3sNJZuI3rGoGwrU@ec2-107-21-222-62.compute-1.amazonaws.com:5432/d13c60av8agdom")

def showAllTables():
	global conn
	cur = conn.cursor()
	cur.execute("SELECT table_name FROM information_schema.tables")
	tables = cur.fetchall()
	tables.sort()
	print( "All Tables" )
	for row in tables:
		print( row )
	print( "------------------------" )

def showAllDocs():
	global conn
	cur = conn.cursor()
	cur.execute("SELECT * FROM uploader_document")
	docs = cur.fetchall()
	print( "All Documents" )
	for doc in docs:
		print( doc )
	print( "------------------------" )

def showAllReports():
	global conn
	cur = conn.cursor()
	cur.execute("SELECT * FROM uploader_report")
	reports = cur.fetchall()
	print( "All Reports" )
	for report in reports:
		print( report )
	print( "------------------------" )

def showAllUsers():
	global conn
	cur = conn.cursor()
	cur.execute("SELECT * FROM auth_user")
	users = cur.fetchall()
	print( "All Users" )
	for user in users:
		print( user )
		print()
	print( "------------------------" )
	
	
	
	
	
	
	
