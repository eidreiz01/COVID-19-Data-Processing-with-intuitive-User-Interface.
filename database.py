
import tui
import sqlite3

def setup_database(records):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	sql_create_table = "CREATE TABLE IF NOT EXISTS covid_19_data (`SNo` integer PRIMARY KEY,`ObservationDate` text,`Province/State` text,`Country/Region` text,`Last Update` text,`Confirmed` integer,`Deaths` integer,`Recovered` integer)"
	cur.execute(sql_create_table)
	for record in records:
		cur.execute("INSERT INTO covid_19_data VALUES (?, ?, ?, ?, ?, ?, ?, ?)", record)

	con.commit()
	con.close()
	return

def unique_country_names():
	try:
		cur = initialise_db()
		cur.execute("SELECT distinct(`Country/Region`) FROM covid_19_data order by `Country/Region` asc")
		return [x[0] for x in cur.fetchall()]
	except:
		return

def cases_by_serial_number():
	try:
		sno = tui.serial_number()
		cur = initialise_db()
		query = "SELECT Confirmed, Deaths, Recovered from covid_19_data where SNo = " + str(sno)
		cur.execute(query)
		return [[x[0],  x[1], x[2]] for x in cur.fetchall()]
	except:
		return

def top_5_countries_by_confirmed_cases():
	try:
		cur = initialise_db()
		cur.execute("SELECT `Country/Region`, sum(Confirmed) FROM covid_19_data group by `Country/Region` order by sum(Confirmed) desc limit 5")
		return [[x[0], x[1]] for x in cur.fetchall()]
	except:
		return

def top_5_countries_by_death_for_specific_dates():
	try:
		dates = tui.observation_dates()
		dates = tuple(dates)
		query = "SELECT `Country/Region`, sum(Deaths) FROM covid_19_data Where ObservationDate IN " + str(dates) + " group by `Country/Region` order by sum(Deaths) desc limit 5"
		cur = initialise_db()
		cur.execute(query)
		return [[x[0], x[1]] for x in cur.fetchall()]
	except:
		return

def cases_by_observation_date():
	try:
		cur = initialise_db()
		query = "SELECT ObservationDate, sum(Confirmed), sum(Deaths), sum(Recovered) FROM covid_19_data where `Country/Region` = 'Mainland China' group by ObservationDate order by ObservationDate asc"
		cur.execute(query)
		return [[x[0], x[1], x[2], x[3]] for x in cur.fetchall()]
	except:
		return

def initialise_db():
	try:
		con = sqlite3.connect("data.db")
		return con.cursor()
	except:
		return