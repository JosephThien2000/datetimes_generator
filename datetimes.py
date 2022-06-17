# import necessary libraries
from datetime import datetime
import os
import pandas as pd
import random as r

# create a list and path for the file
current_path = os.getcwd().replace("\\", "/")
file_path = current_path + "/" + 'datetimes.csv'
thirtyOne_months = [1, 3, 5, 7, 8, 10, 12]
thirty_months = [4, 6, 9, 11]
day_of_week = [ 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# create a date time object and get the current date and time
def create_datetime(elements):
    if os.path.exists(file_path):
        os.remove(file_path)
    try:
        for i in range(int(elements)):
            month = r.randrange(1, 12)
            year = r.randrange(2000, 2022)
            hour = r.randrange(0, 24)
            minute = r.randrange(0, 60)
            second = r.randrange(0, 60)
            if month in thirty_months:
                day = r.randrange(1, 30)
            elif month in thirtyOne_months:
                day = r.randrange(1, 31)
            else:
                day = r.randrange(1, 28)
            if month < 10:
                month = '0' + str(month)
            else:  month = str(month)
            if day < 10:
                day = '0' + str(day)
            else: day = str(day)

            date = f"{year},{month},{day},{hour},{minute},{second},{day_of_week[datetime.weekday(datetime(year, int(month), int(day)))]}"

            os.system("echo {}  >> datetimes.csv".format(date))
        print("datetimes.csv successfully created")
    except Exception as e:
        raise Exception(e)

   
# run __main__ 
# if __name__ == "__main__":
#     while True:
#         num_of_elements = int(input("Enter number of elements: "))
#         if num_of_elements >= 0:
#             break
    
#     datetime_file = create_datetime(num_of_elements)
#     datetime_file