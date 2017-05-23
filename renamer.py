#! python3
# Renamer.py - renames basenames of files in a specified directory to Date Modified.

# TO DO:
# create GUI with Tkinter
# Allow user to input directory
# button to 'Scan'
# visually display list of files
# button to 'Rename'
# visually display renamed files


import os, datetime, sys

Test_mode = False


def set_directory():
    if len(sys.argv) > 1:
        dir = str(sys.argv[1])  # takes the desired directory from the command line argument, passed by the batch file
    else:
        if os.path.exists(r"C:\Program Files\StableBit\DrivePool"):
            print("Kev's Home PC detected, setting default test directory accordingly")
            dir = r"C:\Github local repos\Renamer\test"   # note this this the hardcoded directory for when working on Home PC
        else:
            print("This isn't Kev's Home PC, must be laptop, so setting test default directory accordingly")
            dir = r"C:\KP Python\Renamer\test"
    return dir


def get_stringname(fname):
    modified_time = os.path.getmtime(fname)  # get raw time modified
    modified_date_time = datetime.datetime.fromtimestamp(modified_time) # convert time modified to something readable
    dt_string = str(modified_date_time) # convert this readable time to a string
    shorter_dt_string = dt_string[0:19] # trim to only the first 19 characters
    amended_dt_string = ''              # for removal of colon characters
    for char in shorter_dt_string:      # for removal of colon characters
        if char != ':':                 # for removal of colon characters
            amended_dt_string += char   # for removal of colon characters
    return amended_dt_string


directory = set_directory()
os.chdir(directory) # change cwd to the desired directory
abspath = os.path.abspath('.')  # define abspath

for filename in os.listdir(os.getcwd()):
    original_basename, ext = os.path.splitext(filename) # isolate basename and extensions
    if ext != '.bat':
        original_filename_incl_path = os.path.join(abspath, filename)  # original name incl path
        new_name = get_stringname(filename) + ext                  # define new name
        new_name_incl_path = os.path.join(abspath, new_name)    # new name incl path
        if not Test_mode:
            os.rename(original_filename_incl_path, new_name_incl_path)    # DISABLE FOR TESTING
        print('Renaming {} to {}'.format(original_filename_incl_path, new_name_incl_path))
