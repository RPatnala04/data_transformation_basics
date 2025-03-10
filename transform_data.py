import pandas as pd
import csv
from datetime import datetime



dataframe = pd.read_csv('al_results_2020.csv', index_col='index', low_memory=False) #Using pandas to read .csv

dataframe = dataframe.drop(columns=['Zscore', 'gender', 'syllabus']) # multiple columns dropped (remove columns: Zscore, gender, syllabus)

dataframe = dataframe.dropna() # drops missing values

dataframe = dataframe.to_csv('new_data_file.csv') #transfer the semi-transformed data to a new file  # ,encoding='utf-8'



def rearranged_date(date):
    '''

    :param date: current date values provided
    :return: a formatted date in the "DD:MONTH:YYYY"

    '''

    try:
        date_and_time = datetime.strptime(date, '%d %B %Y') #string to date time object format
        correct_format = True
        print("correct data format")

    # Catches invalid date entries
    except ValueError:
        correct_format = False
    return correct_format



def transform_file(old_file):

    updated_results_2020 = open("updated_results_2020.csv", 'w', newline='') # open new file to write the cleaned data
    csv_writer = csv.writer(updated_results_2020, delimiter=',')

    headers = ["index","stream","sub1","sub1_r","sub_2", "sub2_r", "sub3", "sub3_r","cgt_r","general_english_r",
               "island_rank","district_rank","birth_date"] #updated column headers

    # Add headings to new file.
    csv_writer.writerow(headers)

    try:
        with open(old_file, newline='') as file:
            csv_reader = csv.reader(file, delimiter=",")

            for row in csv_reader: #select rows to rearrange
                if rearranged_date(' '.join(row[10:13])): # join all the date rows (birth_day , birth_month, birth_year)
                    csv_writer.writerow(row[0:10] + row[13:15] + [' '.join(row[10:13])]) # write values to new .csv

    except FileNotFoundError as errmsg:
        print("file not found")
        print(errmsg)
    finally:
        print("Execution complete")

#Function call
transform_file('new_data_file.csv')