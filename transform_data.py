import csv


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




