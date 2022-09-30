def total_number_of_records(records):
	return len(records)


def record_by_serial_number(records, serial_number):
	for record in records:
		if record[0] == str(serial_number):
			return record


def records_by_observation_dates(records, observation_dates):
	list_of_records = []
	for record in records:
		if record[1] in observation_dates:
			list_of_records.append(record)
	return list_of_records


def records_grouped_by_country_region(records):
	records_grouped = {}
	for record in records:
		if record[3] in records_grouped.keys():
			records_grouped[record[3]].append(record)
		else:
			records_grouped[record[3]] = []
			records_grouped[record[3]].append(record)
	records_grouped_list = []
	for key in records_grouped.keys():
		records_grouped_list.extend(records_grouped[key])
	return records_grouped_list


def records_summary(records):
	records_grouped = records_grouped_by_country_region(records)
	records_summary_grouped = []
	country_region = records[0][3]
	confirmed_cases = 0
	death_cases = 0
	recovered_cases = 0
	for record in records_grouped:
		if record[3] == country_region:
			confirmed_cases = confirmed_cases + int(record[5])
			death_cases = death_cases + int(record[6])
			recovered_cases = recovered_cases + int(record[7])
		else:
			records_summary_grouped.extend([0, 0, 0, country_region, 0, confirmed_cases, death_cases, recovered_cases])
			confirmed_cases = int(record[5])
			death_cases = int(record[6])
			recovered_cases = int(record[7])
			country_region = record[3]
	records_summary_grouped.extend([0, 0, 0, country_region, 0, confirmed_cases, death_cases, recovered_cases])
	return records_summary_grouped