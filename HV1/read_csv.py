import csv

# Forward decleration of lists and sets
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

# Function to print relevant keys for easy access
def print_keys():
    print('----- Vinna: Ár -----')
    print(*vinna_ar[:4], sep = '\t')
    print(*vinna_ar[4:8], sep = '\t')
    print(*vinna_ar[8:12], sep = '\t')
    print(*vinna_ar[12:16], sep = '\t')
    print(vinna_ar[16])
    print()
    print()
    print('----- Vinna: Starfsstéttir -----')
    print(*vinna_starfsstett[:4], sep = '\t\t')
    print(*vinna_starfsstett[4:6], sep = '\t')
    print(*vinna_starfsstett[6:], sep = '\t')
    print()
    print()
    print('----- Vinna: Kyn -----')
    print(*vinna_kyn, sep = '\t\t')
    print()
    print()
    print('----- Vinna: Vinnuhlutfall -----')
    print(*vinna_vinnuhlutf, sep = '\n')
    print()
    print()
    print('----- Menntun: Menntunarstig -----')
    print(*menntun_menntun[:2], sep = '\t\t\t\t')
    print(*menntun_menntun[2:4], sep = '\t')
    print(*menntun_menntun[4:], sep = '\t')
    print()
    print()
    print('----- Menntun: Aldur/Búseta -----')
    print(*menntun_aldurbus[:3], sep = '\t\t')
    print(*menntun_aldurbus[3:6], sep = '\t\t')
    print(*menntun_aldurbus[6:9], sep = '\t\t')
    print(*menntun_aldurbus[9:11], sep = '\t\t\t')
    print(*menntun_aldurbus[11:])
    print()
    print()
    print('----- Menntun: Kyn -----')
    print(*menntun_kyn, sep = '\t\t')
    print()
    print()
    print('----- Menntun: Ár -----')
    print(*menntun_ar[:4], sep = '\t')
    print(*menntun_ar[4:8], sep = '\t')
    print(*menntun_ar[8:], sep = '\t')

with open('menntun.csv', 'r', encoding="utf8") as csvfile:
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

with open('laun_alm_vinnum.csv', 'r', encoding="utf8") as csvfile:
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

# Sort lists
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
