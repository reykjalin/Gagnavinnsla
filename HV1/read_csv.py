import csv

menntun = []
menntun_menntun = set()
menntun_aldurbus = set()
menntun_kyn = set()

vinna = []
vinna_ar = set()
vinna_starfsstett = set()
vinna_kyn = set()

def print_keys():
    print('----- Vinna: Ár -----')
    for i in vinna_ar:
        print(i)
    print('----- Vinna: Ár -----')
    print('----- Vinna: Starfsstéttir -----')
    for i in vinna_starfsstett:
        print(i)
    print('----- Vinna: Starfsstéttir -----')
    print('----- Vinna: Kyn -----')
    for i in vinna_kyn:
        print(i)
    print('----- Vinna: Kyn -----')
    print()
    print('----- Menntun: Menntunarstig -----')
    for i in menntun_menntun:
        print(i)
    print('----- Menntun: Menntunarstig -----')
    print('----- Menntun: Aldur/Búseta -----')
    for i in menntun_aldurbus:
        print(i)
    print('----- Menntun: Aldur/Búseta -----')
    print('----- Menntun: Kyn -----')
    for i in menntun_kyn:
        print(i)
    print('----- Menntun: Kyn -----')

with open('menntun.csv', 'r') as csvfile:
    # Use sniffer to find dialect
    currdialect = csv.Sniffer().sniff(csvfile.read(1024))
    # Use seek to go back to beginning of data.csv
    csvfile.seek(0)

    # Initialize the dictreader
    dictreader = csv.DictReader(csvfile, dialect = currdialect)
    
    # Read from csv file
    for row in dictreader:
        menntun.append(row)
        menntun_menntun.add(row['Menntun'])
        menntun_aldurbus.add(row['Aldursflokkur/Búseta'])
        menntun_kyn.add(row['Kyn'])

with open('laun_alm_vinnum.csv', 'r') as csvfile:
    # Sniff
    currdialect = csv.Sniffer().sniff(csvfile.read(1024))
    # Go back
    csvfile.seek(0)

    # Initialize dictreader
    dictreader = csv.DictReader(csvfile, dialect = currdialect)

    # Read csv file
    for row in dictreader:
        vinna.append(row)
        vinna_ar.add(row['Ár'])
        vinna_starfsstett.add(row['Starfsstétt'])
        vinna_kyn.add(row['Kyn'])

menntun_menntun = list(menntun_menntun)
menntun_kyn = list(menntun_kyn)
menntun_aldurbus = list(menntun_aldurbus)
menntun_menntun.sort()
menntun_kyn.sort()
menntun_aldurbus.sort()

vinna_ar = list(vinna_ar)
vinna_kyn = list(vinna_kyn)
vinna_starfsstett = list(vinna_starfsstett)
vinna_ar.sort()
vinna_kyn.sort()
vinna_starfsstett.sort()

print_keys()
