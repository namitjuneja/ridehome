#!/usr/bin/python
import MySQLdb
from flask import request

db = MySQLdb.connect("sql6.freemysqlhosting.net","sql6103440","bqz3y1t3aU","sql6103440" ) # Open database connection

def test_function(request, db = db):
	details = {"name" : request.form["name"], "date" : request.form["date"], "month" : request.form["month"], "year" : request.form["year"], "start_time" : request.form["start_time"], "end_time" : request.form["end_time"], "destination" : request.form["destination"], "number" : request.form["number"], "comments" : request.form["comments"]}
	cursor = db.cursor() # prepare a cursor object using cursor() method
	sql = """INSERT INTO user_data (name, date, month, year, start_time, end_time, destination, contact, comments) 
		VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s);""", (str(request.form["name"]), str(request.form["date"]), str(request.form["month"]), str(request.form["year"]), str(request.form["start_time"]), str(request.form["end_time"]), str(request.form["destination"]), str(request.form["number"]), str(request.form["comments"]))
	cursor.execute(sql) # execute SQL query using execute() method.
	db.commit()
	db.close()  # disconnect from server
	return str(details)

# cursor = db.cursor() # prepare a cursor object using cursor() method
# sql = """INSERT INTO user_data (name, date, month, year, start_time, end_time, destination, contact, comments) VALUES ( '1','1','1','1','1','1','1','1', '1');"""
# sql1 = "insert into user_data values ('1', '2', '3' );"
# cursor.execute(sql) # execute SQL query using execute() method.
# db.commit()
# db.close()  # disconnect from server