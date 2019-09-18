# -*- coding: UTF-8 -*-

# read file
filename = "test.txt"
f = open(filename, 'a') # append model

append_data = '\nPlease append this row.'
f.write(append_data)

f.close()
