import csv


output_file = open("user_with_dates.csv", "w")
csvfile = open('user_OK.csv', 'rb')
spamreader = csv.reader(csvfile, delimiter=',',)
for row in spamreader:
    row[12] = row[12][11:13]
    row = ', '.join(row)

    print row

    output_file.write("%s\n" % row)


