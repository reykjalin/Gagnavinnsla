import csv

headers = {}
menntun = []
with open('menntun.csv', 'r') as csvfile:
    # Use sniffer to find dialect
    currdialect = csv.Sniffer().sniff(csvfile.read(1024))
    # Use seek to go back to beginning of data.csv
    csvfile.seek(0)

    # Initialize the dictreader
    dictreader = csv.DictReader(csvfile, dialect = currdialect)
    
    # Read from csv file
    firstrow = True
    for row in dictreader:
        menntun.append(row)

for i in menntun:
    print(i)
