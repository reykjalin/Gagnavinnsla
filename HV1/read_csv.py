import csv

menntun = []
menntun_menntun = set()
menntun_aldurbus = set()
menntun_kyn = set()
menntun_ar = list()

vinna = []
vinna_ar = set()
vinna_starfsstett = set()
vinna_kyn = set()
vinna_vinnuhlutf = list()

def print_keys():
    print('----- Vinna: Ár -----')
    print(*vinna_ar, sep = '\t|\t')
    print('----- Vinna: Ár -----')
    print()
    print('----- Vinna: Starfsstéttir -----')
    print(*vinna_starfsstett, sep = '\t|\t')
    print('----- Vinna: Starfsstéttir -----')
    print()
    print('----- Vinna: Kyn -----')
    print(*vinna_kyn, sep = '\t|\t')
    print('----- Vinna: Kyn -----')
    print()
    print('----- Vinna: Vinnuhlutfall -----')
    print(*vinna_vinnuhlutf, sep = '\n')
    print('----- Vinna: Vinnuhlutfall -----')
    print()
    print('----- Menntun: Menntunarstig -----')
    print(*menntun_menntun, sep = '\t|\t')
    print('----- Menntun: Menntunarstig -----')
    print()
    print('----- Menntun: Aldur/Búseta -----')
    print(*menntun_aldurbus, sep = '\t|\t')
    print('----- Menntun: Aldur/Búseta -----')
    print()
    print('----- Menntun: Kyn -----')
    print(*menntun_kyn, sep = '\t|\t')
    print('----- Menntun: Kyn -----')
    print()
    print('----- Menntun: Ár -----')
    print(*menntun_ar, sep = '\t|\t')
    print('----- Menntun: Ár -----')    

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
menntun_ar = [x for x in list(menntun[0].keys()) if x.isdigit()]
menntun_ar.sort()
menntun_menntun.sort()
menntun_kyn.sort()
menntun_aldurbus.sort()

vinna_ar = list(vinna_ar)
vinna_kyn = list(vinna_kyn)
vinna_starfsstett = list(vinna_starfsstett)
vinna_vinnuhlutf = [x for x in list(vinna[0].keys()) if x != 'Kyn' and x != 'Starfsstétt' and x != 'Ár']
vinna_vinnuhlutf.sort()
vinna_ar.sort()
vinna_kyn.sort()
vinna_starfsstett.sort()

print_keys()
