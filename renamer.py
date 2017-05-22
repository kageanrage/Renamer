#! python3
# Renamer.py - renames basenames of files in a specified directory to Date Modified.

# TO DO:
# refactor
# create GUI with Tkinter
# Allow user to input directory
# button to 'Scan'
# visually display list of files
# button to 'Rename'
# visually display renamed files


import os, datetime, sys

directory = str(sys.argv[1])  # takes the desired directory from the command line argument, passed by the batch file

os.chdir(directory) # change cwd to the desired directory
abspath = os.path.abspath('.')  # define abspath

for filename in os.listdir(os.getcwd()):
    original_basename, ext = os.path.splitext(filename) # isolate basename and extensions
    if ext != '.bat':
        modified_time = os.path.getmtime(filename)  # get raw time modified
        modified_date_time = datetime.datetime.fromtimestamp(modified_time) # convert time modified to something readable
        dt_string = str(modified_date_time) # convert this readable time to a string
        shorter_dt_string = dt_string[0:19] # trim to only the first 19 characters
        amended_dt_string = ''              # for removal of colon characters
        for char in shorter_dt_string:      # for removal of colon characters
            if char != ':':                 # for removal of colon characters
                amended_dt_string += char   # for removal of colon characters
        original_name = original_basename + ext             # define original name
        original_filename_incl_path = os.path.join(abspath, original_name)  # original name incl path
        new_name = amended_dt_string + ext                  # define new name
        new_name_incl_path = os.path.join(abspath, new_name)    # new name incl path

        # print('New file name:',new_name)

        os.rename(original_filename_incl_path, new_name_incl_path)




