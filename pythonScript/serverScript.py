# Server Script !

import os
import sys
import time

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]
accumulative_file_path = sys.argv[3]
script_file_path = sys.argv[4]

print sys.argv

print input_file_path
print output_file_path
print accumulative_file_path
print script_file_path

while True:
    if os.stat("logged.txt").st_size == 0:
        continue
    else:
        os.system(script_file_path + " " + sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3])
        cleaning_buffer = open(input_file_path, "rw+")
        cleaning_string = cleaning_buffer.read()
        print cleaning_string
        cleaning_buffer.truncate(0)
        cleaning_buffer.close()

