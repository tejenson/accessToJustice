import csv

# for path, input_csv, output_csv and string variables:
#   to hardcode these rather than set them via user input, comment out the active input lines below
#   then uncomment the lines below where these are hardcoded (and modify as needed)

path = input("Enter directory path containing .csv (e.g. /Users/tinlizzy/Downloads/AtoJ/): ")
# path = '/Users/tinlizzy/Downloads/AtoJ/'

input_csv = input("Enter name of csv file (e.g. 1stDCA2017.csv): ")
# input_csv = '1stDCA2017.csv'

output_csv = input("Enter name of output file (e.g. 1stDCA2017_StateOfFlorida_only.csv): ")
# output_csv = '1stDCA2017_StateOfFlorida_only.csv'
                   
string = input("Enter the search string: ")
# string = 'State of Florida'


# opening the input CSV file
with open(path + input_csv, mode ='r')as file1:
   
# reading the input CSV file
  csvFile1 = csv.reader(file1)
 
# search for text string in each row of input csv; if search string present then write that line to new output csv
  for line in csvFile1: # treats each row as a line
        if string in str(line): # checks for the search text in the "stringified" version of the row
            # print(line) # uncomment this line to troubleshoot by viewing rows before trying to write it

            # open new csv file to write/append to
            with open(path + output_csv, 'a', newline='') as write_obj:
                # Create a writer object from csv module
                csv_writer = csv.writer(write_obj)
                # Add contents of list as last row in the csv file
                csv_writer.writerow(line)


        
        

 
