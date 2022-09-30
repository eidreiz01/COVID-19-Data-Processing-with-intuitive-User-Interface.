
import database
import matplotlib.pyplot as plt

def pie_chart_confirmed_cases():
	data = database.top_5_countries_by_confirmed_cases()
	labels = [x[0] for x in data]
	val = [int(x[1]) for x  in data]
	plt.figure(figsize=(16, 16))
	plt.pie(val, labels = None)
	plt.legend(labels=labels)
	plt.title('top 5 countries by confirmed cases')
	plt.show()
	return


def bar_chart_death_cases():
	data = database.top_5_countries_by_death_for_specific_dates()
	labels = [x[0] for x in data]
	val = [int(x[1]) for x  in data]
	plt.figure(figsize=(12, 12))
	plt.bar(labels, val)
	plt.xlabel('Country Name')
	plt.ylabel('Death Count')
	plt.title('top 5 countries by death numbers for specific dates')
	plt.show()

def animated_chart_to_show_changes():
	data = database.cases_by_observation_date()
	labels = [x[0] for x in data]
	confirmed = [int(x[1]) for x in data]
	death = [int(x[2]) for x in data]
	recovered = [int(x[3]) for x in data]
	plt.figure(figsize=(12, 12))
	plt.plot(labels, confirmed, c='b')
	plt.plot(labels, death, c='r')
	plt.plot(labels, recovered, c='g')
	plt.xlabel('Observation Date')
	plt.ylabel('Cases Count')
	plt.title('variation of cases over time')
	plt.legend(labels = ['Confirmed', 'Death', 'Recovered'])
	plt.show()