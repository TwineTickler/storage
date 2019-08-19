# creates an email alert when a new file is detected in the desired directory
#     Created by:
#          Sean Carpenter - 8/19/2019
#     Last Updated by (change log):
#          ---

# Functions
# ---------
# get_directory_contents(dir)
#     arguments: 
#          dir - file path
#     returns:   
#          list containing directory contents
#

# Variables
# ---------
# dir - str - folder path to watch for changes
# contents_master - list - master list of directory contents
#

# Libraries
# ---------
# os
# 

import os

dir = '/home/squall/pyprojects/repos/storage/vod-alerts/testing/'

# upload contents of a dir to a list
def get_directory_contents(dir):
    try:
        contents = os.listdir(dir)
        print('Success')
        return contents
    except:
        print('Error getting directory contents!')
        exit()

contents_master = get_directory_contents(dir)

print(contents_master)
# print(type(dir), type(contents_master), 'list items count: ' + str(len(contents)))
