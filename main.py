
import os
import csv
import tui, process, database, visual

covid_records = []

def run():
    tui.welcome()
    tui.progress("Loading Data", len(covid_records))
    file_path = os.getcwd() + '/data/covid_19_data.csv'
    if os.path.exists(file_path):
        with open(file_path, "r", newline='') as f:
            reader = csv.reader(f, lineterminator='')
            rows = list(reader)
            rows = rows[1:]
            # print(rows[1])
            for i, row in enumerate(rows):
                # print(" ---> ", row)
                covid_records.append(row)
                if i%100 == 0:
                    tui.progress("Loading Data", (len(covid_records)/len(list(rows)))*100)

            tui.progress("Loading Data", (len(covid_records)/len(list(rows)))*100)

    while True:

        opt = tui.menu(0)
        if opt == 1:
            tui.progress("Processing", 0)
            opt1 = tui.menu(1)

            if opt1 == 1:
                tui.progress("Record retrieval process", 0)
                num = tui.serial_number()
                print("NUM : ", num, " type : ", type(num))
                record = process.record_by_serial_number(covid_records, num)
                tui.display_record(record)
                tui.progress("Record retrieval process", 100)

            elif opt1 == 2:
                tui.progress("Records retrieval process", 0)
                dates = tui.observation_dates()
                records = process.records_by_observation_dates(covid_records, dates)
                tui.display_records(records)
                tui.progress("Records retrieval process", 100)

            elif opt1 == 3:
                tui.progress("Grouping process", 0)
                records = process.records_grouped_by_country_region(covid_records)
                tui.display_records(records)
                tui.progress("Grouping process", 100)

            elif opt1 == 4:
                tui.progress("Summary process", 0)
                records = process.records_summary(covid_records)
                tui.display_records(records)
                tui.progress("Summary process", 100)

            else:
                tui.error("Invalid option entered!!")
                continue
            tui.progress("Processing", 100)

        if opt == 2:
            tui.progress("Databse querying operation", 0)
            opt2 = tui.menu(2)

            if opt2 == 1:
                tui.progress("Database initialization process", 0)
                database.setup_database(covid_records)
                tui.progress("Database initialization process", 100)

            elif opt2 == 2:
                tui.progress("Records retrieval process", 0)
                records = database.unique_country_names()
                if not records:
                    tui.error("Database not initialzed!!")
                    continue
                tui.display_records(records)
                tui.progress("Records retrieval process", 100)

            elif opt2 == 3:
                tui.progress("Records retrieval process", 0)
                records = database.cases_by_serial_number()
                if not records:
                    tui.error("Database not initialzed!!")
                    continue
                tui.display_records(records)
                tui.progress("Records retrieval process", 100)

            elif opt2 == 4:
                tui.progress("Records retrieval process", 0)
                records = database.top_5_countries_by_confirmed_cases()
                if not records:
                    tui.error("Database not initialzed!!")
                    continue
                tui.display_records(records)
                tui.progress("Records retrieval process", 100)

            elif opt2 == 5:
                tui.progress("Records retrieval process", 0)
                records = database.top_5_countries_by_death_for_specific_dates()
                if not records:
                    tui.error("Database not initialzed!!")
                    continue
                tui.display_records(records)
                tui.progress("Records retrieval process", 100)

            else:
                tui.error("Invalid option entered!!")
                continue
            tui.progress("Databse querying operation", 100)

        if opt == 3:
            tui.progress("Data visualization operation", 0)
            opt3 = tui.menu(3)

            if opt3 == 1:
                tui.progress("Country/Region pie chart creation", 0)
                visual.pie_chart_confirmed_cases()
                tui.progress("Country/Region pie chart creation", 100)

            elif opt3 == 2:
                tui.progress("Observations chart creation", 0)
                visual.bar_chart_death_cases()
                tui.progress("Observations chart creation", 100)

            elif opt3 == 3:
                tui.progress("Animated summary creation", 0)
                visual.animated_chart_to_show_changes()
                tui.progress("Animated summary creation", 100)

            else:
                tui.error("Invalid option entered!!")
                continue
            tui.progress("Data visualization operation", 100)

        if opt == 4:
            break

        if opt < 1 or opt > 4:
            tui.error("Invalid option entered!!")
        pass  # can remove


if __name__ == "__main__":
    run()
