import sys
import csv
from datetime import datetime

args = sys.argv

file = args[1]
column_number = int(args[2])
from_replace = args[3]
to_replace = args[4]

replaced_file = datetime.now().strftime("%Y%m%d%H%M%S%s") + '.csv'

with open(replaced_file, 'w') as writecsvfile:
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            row[column_number] = row[column_number].replace(from_replace, to_replace)
            print(','.join(row))
            writecsvfile.write(','.join(row) + '\n')
