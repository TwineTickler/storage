# creates an email alert when a new file is detected in the desired directory
#     Created by:
#          Sean Carpenter - 8/19/2019
#     Last Updated by (change log):
#          ---

# Functions
# ---------
# get_directory_contents()
#     arguments: 
#          dir - file path
#     returns:   
#          list containing directory contents
#
# get_only_mp4_files()
#     arguments:
#          lst - list of folder contents
#     returns:
#          list containing only file names ending in .mp4
#
# is_file_new() - used to determine if a file is new or renamed. If new returns True
#     arguments:
#          filename - name of file in question
#     returns:
#          True or False

# Variables
# ---------
# frequency ------ :int:  number of seconds to wait before checking for new files in the directory
# dir ------------ :str:  folder path to watch for changes
# contents_master  :list: master list of directory contents
# contents_current :list: current list of directory contents
# looper --------- :bool: used to stop the while loop (True/False)

# Modules
# -------
# os
# time

import os
import time

print('VOD-alerts-v1 running. Use ctrl+c to quit...')
dir = '/home/squall/pyprojects/repos/storage/vod-alerts/testing/'
frequency = int(3) # int - number of seconds to check the file structure for new content

# upload contents of a dir to a list
def get_directory_contents(dir):
    try:
        contents = os.listdir(dir)
        return contents
    except:
        print('Error getting directory contents!')
        exit()

def get_only_mp4_files(lst):
    result = []
    for item in lst:
        if item.endswith('.mp4'):
            result.append(item)
    return result

def is_file_new(filename):
    # compare date created with date modified
    filepath = dir + filename
    if os.stat(filepath).st_ctime == os.stat(filepath).st_mtime:
        return True
    else:
        return False

# get inital folder contents
contents_master = get_only_mp4_files(get_directory_contents(dir))

# check the contents of the folder once a minute
# and compare the contents to the master
# then update the master from the current
looper = True
while looper:
    try:
        # get current folder contents
        contents_current = get_only_mp4_files(get_directory_contents(dir))
        # do they not equal eachother?
        if contents_current != contents_master:
            # changes detected!
            # whatever is in current but not in master are new files
            for item in contents_current:
                if item not in contents_master:
                    # possible new file detected
                    if is_file_new(item):
                        print(item)

        time.sleep(frequency)
        contents_master = contents_current
    # Error handling
    except KeyboardInterrupt:
        looper = False
        print('\nProcess ended by user. Exiting...')
    except:
        looper = False
        print('\nError detected in loop, exiting...')

# print(contents_master)
# print(type(dir), type(contents_master), 'list items count: ' + str(len(contents)))
