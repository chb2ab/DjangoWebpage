import psycopg2
import urllib.request
import json
import requests

from helpers import showAllTables, showAllDocs, showAllReports, showAllUsers
from decrypt import decrypt_file
from encrypt import encrypt_file

# postgres://wxpgtsbsjogwtq:I9eTFdgCmBvmHfJtvynY5xlR3e@ec2-107-21-222-62.compute-1.amazonaws.com:5432/dh7aknrqvagc7

# postgres://fqrrqdnannsmis:ZaUeBB7LVhfLXrQrOAWfeHQmXk@ec2-107-21-219-142.compute-1.amazonaws.com:5432/d8q06ijrlprkik

# postgres://hvcaoxvgdsxzui:ZnOM8mecGoc3sNJZuI3rGoGwrU@ec2-107-21-222-62.compute-1.amazonaws.com:5432/d13c60av8agdom


global conn
conn = psycopg2.connect("postgres://hvcaoxvgdsxzui:ZnOM8mecGoc3sNJZuI3rGoGwrU@ec2-107-21-222-62.compute-1.amazonaws.com:5432/d13c60av8agdom")
	
def save_file( text, name ):
	fw = open("downloads/"+name, 'wb');
	fw.write(text);
	return True;
	
def getDocs( report ):
	global conn
	cur = conn.cursor()
	cur.execute("SELECT * FROM uploader_document")
	docs = cur.fetchall()
	documents = []
	for doc in docs:
		if ( doc[2] == report[0] ):
			documents.append(doc)
	return(documents)

def getPublicReports():
	global conn
	cur = conn.cursor()
	cur.execute("SELECT * FROM uploader_report")
	reports = cur.fetchall()
	publicReports = []
	for report in reports:
		if( report[4] == True ):
			publicReports.append(report)
	return(publicReports)

if __name__ == "__main__":
	showAllDocs()






