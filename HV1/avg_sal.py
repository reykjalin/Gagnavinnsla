import read_csv as data
import dict_sort
import list_to_int as lti
import matplotlib.pyplot as plt

# Declare all dictionaries that will store data
avg_all = dict()
avg_kvk = dict()
avg_kk = dict()
avg2_all = dict()
avg2_kvk = dict()
avg2_kk = dict()
stjorn_all = dict()
stjorn_kk = dict()
stjorn_kvk = dict()
serfr_all = dict()
serfr_kk = dict()
serfr_kvk = dict()

# Get data
for row in data.vinna:
    if row['Starfsstétt'] == 'Alls':
        if row['Kyn'] == 'Alls':
            avg_all[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
        elif row['Kyn'] == 'Karlar':
            avg_kk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
        elif row['Kyn'] == 'Konur':
            avg_kvk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
    elif row['Starfsstétt'] != 'Verkafólk' and row['Starfsstétt'] != 'Iðnaðarmenn':
        if row['Kyn'] == 'Alls':
            avg2_all[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
        elif row['Kyn'] == 'Karlar':
            avg2_kk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
        elif row['Kyn'] == 'Konur':
            avg2_kvk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
    if row['Starfsstétt'] == 'Stjórnendur':
        if row['Kyn'] == 'Alls':
            stjorn_all[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
        elif row['Kyn'] == 'Karlar':
            stjorn_kk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
        elif row['Kyn'] == 'Konur':
            stjorn_kvk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
    elif row['Starfsstétt'] == 'Sérfræðingar':
        if row['Kyn'] == 'Alls':
            serfr_all[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
        elif row['Kyn'] == 'Karlar':
            serfr_kk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
        elif row['Kyn'] == 'Konur':
            serfr_kvk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']

# Sort dictionaries and get lists
avg_all = dict_sort.key_sort(avg_all)
avg_kk = dict_sort.key_sort(avg_kk)
avg_kvk = dict_sort.key_sort(avg_kvk)
avg2_all = dict_sort.key_sort(avg2_all)
avg2_kk = dict_sort.key_sort(avg2_kk)
avg2_kvk = dict_sort.key_sort(avg2_kvk)
stjorn_all = dict_sort.key_sort(stjorn_all)
stjorn_kk = dict_sort.key_sort(stjorn_kk)
stjorn_kvk = dict_sort.key_sort(stjorn_kvk)
serfr_all = dict_sort.key_sort(serfr_all)
serfr_kk = dict_sort.key_sort(serfr_kk)
serfr_kvk = dict_sort.key_sort(serfr_kvk)

# Change lists to int
avg_all = lti.tuple2_toint(avg_all)
avg_kk = lti.tuple2_toint(avg_kk)
avg_kvk = lti.tuple2_toint(avg_kvk)
avg2_all = lti.tuple2_toint(avg2_all)
avg2_kk = lti.tuple2_toint(avg2_kk)
avg2_kvk = lti.tuple2_toint(avg2_kvk)
stjorn_all = lti.tuple2_toint(stjorn_all)
stjorn_kk = lti.tuple2_toint(stjorn_kk)
stjorn_kvk = lti.tuple2_toint(stjorn_kvk)
serfr_all = lti.tuple2_toint(serfr_all)
serfr_kk = lti.tuple2_toint(serfr_kk)
serfr_kvk = lti.tuple2_toint(serfr_kvk)

def plot_avg_all():
    x = list()
    y = list()
    for i in range(len(avg_all)):
        x.append(avg_all[i][0])
        y.append(avg_all[i][1])
    plt.plot(x, y)#, align = 'center')

def plot_avg_kk():
    xkk = list()
    ykk = list()
    for i in range(len(avg_kk)):
        xkk.append(avg_kk[i][0])
        ykk.append(avg_kk[i][1])
    plt.plot(xkk, ykk)#,align = 'center')

def plot_avg_kvk():
    xkvk = list()
    ykvk = list()
    for i in range(len(avg_kvk)):
        xkvk.append(avg_kvk[i][0])
        ykvk.append(avg_kvk[i][1])
    plt.plot(xkvk, ykvk)#,align = 'center')

def plot_avg2_all():
    x2 = list()
    y2 = list()
    for i in range(len(avg2_all)):
        x2.append(avg2_all[i][0])
        y2.append(avg2_all[i][1])
    plt.plot(x2, y2)

def plot_avg2_kk():
    x2kk = list()
    y2kk = list()
    for i in range(len(avg2_kk)):
        x2kk.append(avg2_kk[i][0])
        y2kk.append(avg2_kk[i][1])
    plt.plot(x2kk, y2kk)

def plot_avg2_kvk():
    x2kvk = list()
    y2kvk = list()
    for i in range(len(avg2_kvk)):
        x2kvk.append(avg2_kvk[i][0])
        y2kvk.append(avg2_kvk[i][1])
    plt.plot(x2kvk, y2kvk)

def plot_stjorn_all():
    xstjorn = list()
    ystjorn = list()
    for i in range(len(stjorn_all)):
        xstjorn.append(stjorn_all[i][0])
        ystjorn.append(stjorn_all[i][1])
    plt.plot(xstjorn, ystjorn)

def plot_stjorn_kk():
    xstjornkk = list()
    ystjornkk = list()
    for i in range(len(stjorn_kk)):
        xstjornkk.append(stjorn_kk[i][0])
        ystjornkk.append(stjorn_kk[i][1])
    plt.plot(xstjornkk, ystjornkk)

def plot_stjorn_kvk():
    xstjornkvk = list()
    ystjornkvk = list()
    for i in range(len(stjorn_kvk)):
        xstjornkvk.append(stjorn_kvk[i][0])
        ystjornkvk.append(stjorn_kvk[i][1])
    plt.plot(xstjornkvk, ystjornkvk)

def plot_serfr_all():
    xserfr = list()
    yserfr = list()
    for i in range(len(serfr_all)):
        xserfr.append(serfr_all[i][0])
        yserfr.append(serfr_all[i][1])
    plt.plot(xserfr, yserfr)

def plot_serfr_kk():
    xserfrkk = list()
    yserfrkk = list()
    for i in range(len(serfr_kk)):
        xserfrkk.append(serfr_kk[i][0])
        yserfrkk.append(serfr_kk[i][1])
    plt.plot(xserfrkk, yserfrkk)

def plot_serfr_kvk():
    xserfrkvk = list()
    yserfrkvk = list()
    for i in range(len(serfr_kvk)):
        xserfrkvk.append(serfr_kvk[i][0])
        yserfrkvk.append(serfr_kvk[i][1])
    plt.plot(xserfrkvk, yserfrkvk)

# Create plots
plt.figure()

plt.subplot(2,1,1)
plot_avg_all()
plot_avg_kk()
plot_avg_kvk()
plt.title('Heildarlaun - Meðaltal í fullri vinnu milli ára í þús. kr.')
plt.legend( ('Alls', 'Karlar', 'Konur'), loc = 'upper left' )

plt.subplot(2,1,2)
plot_avg2_all()
plot_avg2_kk()
plot_avg2_kvk()
plt.title('Skrifstofufólk, Stjórnendur, Sérfræðingar, Tæknar og sérmenntað starfsfólk, Þjónustu-, sölu- og afgreiðslufólk')
plt.legend( ('Alls', 'Karlar', 'Konur'), loc = 'upper left' )


plt.figure()

plt.subplot(2,1,1)
plot_stjorn_all()
plot_stjorn_kk()
plot_stjorn_kvk()
plt.legend( ('Alls', 'Karlar', 'Konur'), loc = 'upper left' )
plt.title('Stjórnendur')

plt.subplot(2,1,2)
plot_serfr_all()
plot_serfr_kk()
plot_serfr_kvk()
plt.legend( ('Alls', 'Karlar', 'Konur'), loc = 'upper left' )
plt.title('Sérfræðingar')

plt.show()
        
# Print keys and relevant information
print()
print()
data.print_keys()
