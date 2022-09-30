
from datetime import datetime

def welcome():
    title = "COVID-19 (January) Data"
    dashes = '-'*len(title)
    print(dashes)
    print(title)
    print(dashes)
    pass


def error(msg):
    print('Error! {0}'.format(msg))
    pass


def progress(operation, value):
    if value == 0:
        print(operation, "has started")
    elif value == 100:
        print(operation, "has completed")
    elif value > 0 and value < 100:
        print(operation, "is in progress {0}% completed".format(value))
    else:
        error("Invalid value passed!!")
    pass


def menu(variant=0):
    if variant == 0:
        option = input("[1] Process Data\n[2] Query Database\n[3] Visualise Data\n[4] Exit\n")
    elif variant == 1:
        option = input("[1] Record by Serial Number\n[2] Records by Observation Date\n[3] Group Records by Country/Region\n[4] Summarise Records\n")
    elif variant == 2:
        option = input("[1] Setup database'\n[2] Retrieve all countries in alphabetical order from the database\n[3] Retrieve confirmed cases, deaths and recoveries for an observation from the database\n[4] Retrieve top 5 countries for confirmed cases from the database from the database\n[5] Retrieve top 5 countries for deaths for specific observation dates form the database\n")
    elif variant == 3:
        option = input("[1] Country/Region Pie Chart\n[2] Observations Chart\n[3] Animated Summary\n")
    else:
        error("Invalid option entered!!")
        return

    try:
        selection = int(option)
        return selection
    except ValueError:
        error("Invalid value entered")
    pass


def total_records(num_records):
    print("There are {0} records in the data set.".format(num_records))
    pass


def serial_number():
    try:
        ser_num = int(input("Enter a serial number : "))
        return ser_num
    except ValueError:
        error("Invalid input entered!!")
    pass


def observation_dates():
    list_of_dates = []
    try:
        num = int(input("Enter the number of dates you want to input: "))
        for i in range(num):
            d = input("Enter the date in format mm/dd/yyyy: ")
            try:
                if len(d) == 10: 
                    datetime.strptime(d, '%m/%d/%Y')
                    list_of_dates.append(d)
                else:
                    error("Invalid Date entered!!")
                    return
            except ValueError:
                error("Invalid date entered!!")
                return

    except ValueError:
        error("Invalid date entered!!")
        return
    return list_of_dates

def display_record(record, cols=None):
    if not cols:
        print(record)
    else:
        cols_to_print = [record[i] for i in cols]
        print(cols_to_print)
    pass


def display_records(records, cols=None):
    if records:
        for record in records:
            display_record(record, cols)