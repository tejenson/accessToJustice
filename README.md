# accessToJustice
Coding to support Mitchell Hamline Access to Justice incubator course

search_string_csv_v1.1.py: 
  + prompts for entry of :
    - directory path where your input .csv file is located
    - name of .csv file 
    - name of a new output .csv file that will be created just with the rows containing the search string of interest
    - text string to search for
  + searches the input csv file for the string (e.g. State of Florida)
  + copies rows containing text to new output csv file

search_jsonFiles_convert_to_csv.py
  + Search a user-defined path for files of a certain type for a text string
  + Kick out a file (filelist.txt) with the list of filenames that have the search string of interest in them. 
    - If the file exists, append to it; if no file, create it. 
    - Drops this file in the user entered path.
  + if search string present
    - run the .json-to-.csv conversion  
    - append contents of json file to a single csv file. 
    - If the file exists, append to it; if no file, create it. 
  + It drops this file in the user entered path.
