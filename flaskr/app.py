from flask import Flask
import sqlite3

app = Flask(__name__)

def list_of_tuples_id_tasks_with_succes_number_sorted():
	conn = sqlite3.connect('schema.sqlite')
	cursor = conn.cursor()

	succes_frequency = {}

	for row in cursor.execute("SELECT DISTINCT task FROM submissions"):
		succes_frequency[row[0]] = None
	for row in cursor.execute("SELECT task, result FROM submissions WHERE result LIKE '%succes%'"):
		if succes_frequency[row[0]] == None:
			succes_frequency[row[0]] = 1
		else :
			succes_frequency[row[0]] += 1
	conn.close()
	sorted_succes_frequency = sorted(succes_frequency.items(), key = lambda kv:(kv[1], kv[0]))
	return sorted_succes_frequency


@app.route("/")
def 