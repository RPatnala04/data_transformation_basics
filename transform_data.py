import pandas as pd
import csv


dataframe = pd.read_csv('al_results_2020.csv', index_col='index', low_memory=False) #Using pandas to read .csv

# remove columns: Zscore, gender, syllabus
dataframe = dataframe.drop(columns=['Zscore', 'gender', 'syllabus']) # multiple columns dropped

dataframe = dataframe.dropna() # drops missing values

dataframe = dataframe.to_csv('new_data_file.csv') #transfer the semi-transformed data to a new file  # ,encoding='utf-8'




def transform_file(old_file):

    updated_results_2020 = open("updated_results_2020.csv", 'w', newline='') # open new file to write the cleaned data
    csv_writer = csv.writer(updated_results_2020, delimiter=',')

    headers = ["index","stream","sub1","sub1_r","sub_2", "sub2_r", "sub3", "sub3_r","cgt_r","general_english_r",
               "birth_date","gender","island_rank","district_rank"] #updated column headers

    csv_writer.writerow(headers) # write the headers to new file

#    data = pd.read_csv('al_results_2020.csv')
#    data.drop('year', inplace=True, axis=1) # dataframe data..
    # make new .csv after cleaning...




    try:
        with open(old_file,newline='') as file:
            csv_reader = csv.reader(file, delimiter=',')

            # Continue here.
            for row in csv_reader:
                if row is not None:



    except FileNotFoundError as errmsg:
        print(errmsg)

    finally:
        updated_results_2020.close()


transform_file('new_file.csv')




