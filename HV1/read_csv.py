import csv

with open('data.csv', 'r') as csvfile:
    # Use sniffer to find dialect
    currdialect = csv.Sniffer().sniff(csvfile.read(1024))
    # Use seek to go back to beginning of data.csv
    csvfile.seek(0)

    # Initialize the dictreader
    dictreader = csv.DictReader(csvfile, dialect = currdialect)
    
    # Read from csv file
    firstrow = True
    for row in dictreader:
        if firstrow:
            firstrow = False
            print(row)
        if row['2013 Alls'].isdigit() and row['Skóli'] == 'Háskólinn í Reykjavík' and int(row['2013 Alls']) > 0:
            print(row['Skóli'], row['Námsbrautir og gráður'], row['2013 Alls'], sep=' <==> ')
