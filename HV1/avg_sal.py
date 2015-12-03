import read_csv as data
import dict_sort
import list_to_int as lti
import matplotlib.pyplot as plt
import plotter
import spurningarjon as sj

def average_sal(figure_number):
    arkk = sj.ArKK
    fjkk = sj.FjKK
    arkvk = sj.ArKvK
    fjkvk = sj.FjKvK

    for i in range(len(fjkvk)):
        arkvk[i] -= 0.05

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
    idnad_all = dict()
    idnad_kk = dict()
    idnad_kvk = dict()
    skrifst_all = dict()
    skrifst_kk = dict()
    skrifst_kvk = dict()
    taeknar_all = dict()
    taeknar_kk = dict()
    taeknar_kvk = dict()
    verka_all = dict()
    verka_kk = dict()
    verka_kvk = dict()
    solu_all = dict()
    solu_kk = dict()
    solu_kvk = dict()

    legend_handles = list()
    plot_title = list()

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
        elif row['Starfsstétt'] == 'Iðnaðarmenn':
            if row['Kyn'] == 'Alls':
                idnad_all[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
            elif row['Kyn'] == 'Karlar':
                idnad_kk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
            elif row['Kyn'] == 'Konur':
                idnad_kvk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
        elif row['Starfsstétt'] == 'Skrifstofufólk':
            if row['Kyn'] == 'Alls':
                skrifst_all[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
            elif row['Kyn'] == 'Karlar':
                skrifst_kk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
            elif row['Kyn'] == 'Konur':
                skrifst_kvk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
        elif row['Starfsstétt'] == 'Tæknar og sérmenntað starfsfólk':
            if row['Kyn'] == 'Alls':
                taeknar_all[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
            elif row['Kyn'] == 'Karlar':
                taeknar_kk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
            elif row['Kyn'] == 'Konur':
                taeknar_kvk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
        elif row['Starfsstétt'] == 'Verkafólk':
            if row['Kyn'] == 'Alls':
                verka_all[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
            elif row['Kyn'] == 'Karlar':
                verka_kk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
            elif row['Kyn'] == 'Konur':
                verka_kvk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
        elif row['Starfsstétt'] == 'Þjónustu-, sölu- og afgreiðslufólk':
            if row['Kyn'] == 'Alls':
                solu_all[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
            elif row['Kyn'] == 'Karlar':
                solu_kk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']
            elif row['Kyn'] == 'Konur':
                solu_kvk[row['Ár']] = row['Heildarlaun - fullvinnandi Meðaltal']

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
    idnad_all = dict_sort.key_sort(idnad_all)
    idnad_kk = dict_sort.key_sort(idnad_kk)
    idnad_kvk = dict_sort.key_sort(idnad_kvk)
    skrifst_all = dict_sort.key_sort(skrifst_all)
    skrifst_kk = dict_sort.key_sort(skrifst_kk)
    skrifst_kvk = dict_sort.key_sort(skrifst_kvk)
    taeknar_all = dict_sort.key_sort(taeknar_all)
    taeknar_kk = dict_sort.key_sort(taeknar_kk)
    taeknar_kvk = dict_sort.key_sort(taeknar_kvk)
    verka_all = dict_sort.key_sort(verka_all)
    verka_kk = dict_sort.key_sort(verka_kk)
    verka_kvk = dict_sort.key_sort(verka_kvk)
    solu_all = dict_sort.key_sort(solu_all)
    solu_kk = dict_sort.key_sort(solu_kk)
    solu_kvk = dict_sort.key_sort(solu_kvk)

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
    idnad_all = lti.tuple2_toint(idnad_all)
    idnad_kk = lti.tuple2_toint(idnad_kk)
    idnad_kvk = lti.tuple2_toint(idnad_kvk)
    skrifst_all = lti.tuple2_toint(skrifst_all)
    skrifst_kk = lti.tuple2_toint(skrifst_kk)
    skrifst_kvk = lti.tuple2_toint(skrifst_kvk)
    taeknar_all = lti.tuple2_toint(taeknar_all)
    taeknar_kk = lti.tuple2_toint(taeknar_kk)
    taeknar_kvk = lti.tuple2_toint(taeknar_kvk)
    verka_all = lti.tuple2_toint(verka_all)
    verka_kk = lti.tuple2_toint(verka_kk)
    verka_kvk = lti.tuple2_toint(verka_kvk)
    solu_all = lti.tuple2_toint(solu_all)
    solu_kk = lti.tuple2_toint(solu_kk)
    solu_kvk =lti.tuple2_toint(solu_kvk)

    def plot_skrifst_all():
        x = list()
        y = list()
        for i in range(len(skrifst_all)):
            x.append(skrifst_all[i][0])
            y.append(skrifst_all[i][1])
        plt.plot(x, y)
        plot_title.append('Skrifstofufólk - Alls')
        legend_handles.append('Skrifstofufólk - Alls')

    def plot_skrifst_kk():
        x = list()
        y = list()
        for i in range(len(skrifst_kk)):
            x.append(skrifst_kk[i][0])
            y.append(skrifst_kk[i][1])
        plt.plot(x, y)
        plot_title.append('Skrifstofufólk - Karlar')
        legend_handles.append('Skrifstofufólk - Karlar')

    def plot_skrifst_kvk():
        x = list()
        y = list()
        for i in range(len(skrifst_kvk)):
            x.append(skrifst_kvk[i][0])
            y.append(skrifst_kvk[i][1])
        plt.plot(x, y)
        plot_title.append('Skrifstofufólk - Konur')
        legend_handles.append('Skrifstofufólk - Konur')

    def plot_taeknar_all():
        x = list()
        y = list()
        for i in range(len(taeknar_all)):
            x.append(taeknar_all[i][0])
            y.append(taeknar_all[i][1])
        plt.plot(x, y)
        plot_title.append('Tæknar og sérm. starfsf. - Alls')
        legend_handles.append('Tæknar og sérm. starfsf. - Alls')

    def plot_taeknar_kk():
        x = list()
        y = list()
        for i in range(len(taeknar_kk)):
            x.append(taeknar_kk[i][0])
            y.append(taeknar_kk[i][1])
        plt.plot(x, y)
        plot_title.append('Tæknar og sérm. starfsf. - Karlar')
        legend_handles.append('Tæknar og sérm. starfsf. - Karlar')

    def plot_taeknar_kvk():
        x = list()
        y = list()
        for i in range(len(taeknar_kvk)):
            x.append(taeknar_kvk[i][0])
            y.append(taeknar_kvk[i][1])
        plt.plot(x, y)
        plot_title.append('Tæknar og sérm. starfsf. - Konur')
        legend_handles.append('Tæknar og sérm. starfsf. - Konur')

    def plot_verka_all():
        x = list()
        y = list()
        for i in range(len(verka_all)):
            x.append(verka_all[i][0])
            y.append(verka_all[i][1])
        plt.plot(x, y)
        plot_title.append('Verkafólk - Alls')
        legend_handles.append('Verkafólk - Alls')

    def plot_verka_kk():
        x = list()
        y = list()
        for i in range(len(verka_kk)):
            x.append(verka_kk[i][0])
            y.append(verka_kk[i][1])
        plt.plot(x, y)
        plot_title.append('Verkafólk - Karlar')
        legend_handles.append('Verkafólk - Karlar')

    def plot_verka_kvk():
        x = list()
        y = list()
        for i in range(len(verka_kvk)):
            x.append(verka_kvk[i][0])
            y.append(verka_kvk[i][1])
        plt.plot(x, y)
        plot_title.append('Verkafólk - Konur')
        legend_handles.append('Verkafólk - Konur')

    def plot_solu_all():
        x = list()
        y = list()
        for i in range(len(solu_all)):
            x.append(solu_all[i][0])
            y.append(solu_all[i][1])
        plt.plot(x, y)
        plot_title.append('Sölufólk - Alls')
        legend_handles.append('Sölufólk - Alls')

    def plot_solu_kk():
        x = list()
        y = list()
        for i in range(len(solu_kk)):
            x.append(solu_kk[i][0])
            y.append(solu_kk[i][1])
        plt.plot(x, y)
        plot_title.append('Sölufólk - Karlar')
        legend_handles.append('Sölufólk - Karlar')

    def plot_solu_kvk():
        x = list()
        y = list()
        for i in range(len(solu_kvk)):
            x.append(solu_kvk[i][0])
            y.append(solu_kvk[i][1])
        plt.plot(x, y)
        plot_title.append('Sölufólk - Konur')
        legend_handles.append('Sölufólk - Konur')

    def plot_idnad_kvk():
        x = list()
        y = list()
        for i in range(len(idnad_kvk)):
            x.append(idnad_kvk[i][0])
            y.append(idnad_kvk[i][1])
        plt.plot(x, y)
        plot_title.append('Iðnaðarmenn - Konur')
        legend_handles.append('Iðnaðarmenn - Konur')

    def plot_idnad_kk():
        x = list()
        y = list()
        for i in range(len(idnad_kk)):
            x.append(idnad_kk[i][0])
            y.append(idnad_kk[i][1])
        plt.plot(x, y)#, align = 'center')
        plot_title.append('Iðnaðarmenn - Karlar')
        legend_handles.append('Iðnaðarmenn - Karlar')

    def plot_idnad_all():
        x = list()
        y = list()
        for i in range(len(idnad_all)):
            x.append(idnad_all[i][0])
            y.append(idnad_all[i][1])
        plt.plot(x, y)#, align = 'center')
        plot_title.append('Iðnaðarmenn - Alls')
        legend_handles.append('Iðnaðarmenn - Alls')

    def plot_avg_all():
        x = list()
        y = list()
        for i in range(len(avg_all)):
            x.append(avg_all[i][0])
            y.append(avg_all[i][1])
        plt.plot(x, y)#, align = 'center')
        plot_title.append('Alls - Alls')
        legend_handles.append('Alls - Alls')

    def plot_avg_kk():
        xkk = list()
        ykk = list()
        for i in range(len(avg_kk)):
            xkk.append(avg_kk[i][0])
            ykk.append(avg_kk[i][1])
        plt.plot(xkk, ykk)#,align = 'center')
        plot_title.append('Alls - Karlar')
        legend_handles.append('Alls - Karlar')

    def plot_avg_kvk():
        xkvk = list()
        ykvk = list()
        for i in range(len(avg_kvk)):
            xkvk.append(avg_kvk[i][0])
            ykvk.append(avg_kvk[i][1])
        plt.plot(xkvk, ykvk)#,align = 'center')
        plot_title.append('Alls - Konur')
        legend_handles.append('Alls - Konur')

    def plot_avg2_all():
        x2 = list()
        y2 = list()
        for i in range(len(avg2_all)):
            x2.append(avg2_all[i][0])
            y2.append(avg2_all[i][1])
        plt.plot(x2, y2)
        plot_title.append('Sérgögn - Alls')
        legend_handles.append('Sérgögn - Alls')

    def plot_avg2_kk():
        x2kk = list()
        y2kk = list()
        for i in range(len(avg2_kk)):
            x2kk.append(avg2_kk[i][0])
            y2kk.append(avg2_kk[i][1])
        plt.plot(x2kk, y2kk)
        plot_title.append('Sérgögn - Karlar')
        legend_handles.append('Sérgögn - Karlar')

    def plot_avg2_kvk():
        x2kvk = list()
        y2kvk = list()
        for i in range(len(avg2_kvk)):
            x2kvk.append(avg2_kvk[i][0])
            y2kvk.append(avg2_kvk[i][1])
        plt.plot(x2kvk, y2kvk)
        plot_title.append('Sérgögn - Konur')
        legend_handles.append('Sérgögn - Konnur')

    def plot_stjorn_all():
        xstjorn = list()
        ystjorn = list()
        for i in range(len(stjorn_all)):
            xstjorn.append(stjorn_all[i][0])
            ystjorn.append(stjorn_all[i][1])
        plt.plot(xstjorn, ystjorn)
        plot_title.append('Stjórnendur - Alls')
        legend_handles.append('Stjórnendur - Alls')

    def plot_stjorn_kk():
        xstjornkk = list()
        ystjornkk = list()
        for i in range(len(stjorn_kk)):
            xstjornkk.append(stjorn_kk[i][0])
            ystjornkk.append(stjorn_kk[i][1])
        plt.plot(xstjornkk, ystjornkk)
        plot_title.append('Stjórnendur - Karlar')
        legend_handles.append('Stjórnendur - Karlar')

    def plot_stjorn_kvk():
        xstjornkvk = list()
        ystjornkvk = list()
        for i in range(len(stjorn_kvk)):
            xstjornkvk.append(stjorn_kvk[i][0])
            ystjornkvk.append(stjorn_kvk[i][1])
        plt.plot(xstjornkvk, ystjornkvk)
        plot_title.append('Stjórnendur - Konur')
        legend_handles.append('Stjórnendur - Konur')

    def plot_serfr_all():
        xserfr = list()
        yserfr = list()
        for i in range(len(serfr_all)):
            xserfr.append(serfr_all[i][0])
            yserfr.append(serfr_all[i][1])
        plt.plot(xserfr, yserfr)
        plot_title.append('Sérfræðingar - Alls')
        legend_handles.append('Sérfræðingar - Alls')

    def plot_serfr_kk():
        xserfrkk = list()
        yserfrkk = list()
        for i in range(len(serfr_kk)):
            xserfrkk.append(serfr_kk[i][0])
            yserfrkk.append(serfr_kk[i][1])
        plt.plot(xserfrkk, yserfrkk)
        plot_title.append('Sérfræðingar - Karlar')
        legend_handles.append('Sérfræðingar - Karlar')

    def plot_serfr_kvk():
        xserfrkvk = list()
        yserfrkvk = list()
        for i in range(len(serfr_kvk)):
            xserfrkvk.append(serfr_kvk[i][0])
            yserfrkvk.append(serfr_kvk[i][1])
        plt.plot(xserfrkvk, yserfrkvk)
        plot_title.append('Sérfræðingar - Konur')
        legend_handles.append('Sérfræðingar - Konur')


        
    # Create plots
    # Figure 1
    plt.figure(figure_number)

    # # Subplot 1.1
    # plt.subplot(2,1,1)
    plot_avg_all()
    plot_avg_kk()
    plot_avg_kvk()
    plt.legend(legend_handles, loc = 'upper left')
    plt.ylabel('Meðallaun í þús. kr.')

    plt.twinx()
    plt.ylabel('Fjöldi háskólamenntaðra einstaklinga')
    plt.bar(arkk, fjkk, width=0.1)
    plt.bar(arkvk, fjkvk, width=0.1, align='center', color = 'red')
    plt.legend(('Fj. Hásk.mennt. Karla','Fj. Hásk.mennt. Kvenna'), loc='center left')
    plt.title(', '.join(plot_title))
    plot_title = list()
    legend_handles = list()
    

    # # Subplot 1.2
    # plt.subplot(2,1,2)
    # plot_avg2_all()
    # plot_avg2_kk()
    # plot_avg2_kvk()
    # plt.title(', '.join(plot_title))
    # plt.legend(legend_handles, loc = 'upper left')
    # plot_title = list()
    # legend_handles = list()


    # # Figure 2
    # plt.figure()

    # # Subplot 2.1
    # plt.subplot(2,1,1)
    # plot_stjorn_all()
    # plot_stjorn_kk()
    # plot_stjorn_kvk()
    # plt.title(', '.join(plot_title))
    # plt.legend(legend_handles, loc = 'upper left')
    # plot_title = list()
    # legend_handles = list()

    # # Subplot 2.2
    # plt.subplot(2,1,2)
    # plot_serfr_all()
    # plot_serfr_kk()
    # plot_serfr_kvk()
    # plt.title(', '.join(plot_title))
    # plt.legend(legend_handles, loc = 'upper left')
    # plot_title = list()
    # legend_handles = list()


    # # Figure 3
    # plt.figure()

    # # Subplot 3.1
    # plt.subplot(2,1,1)
    # plot_idnad_all()
    # plot_idnad_kk()
    # plot_idnad_kvk()
    # plt.title(', '.join(plot_title))
    # plt.legend(legend_handles, loc = 'upper left')
    # plot_title = list()
    # legend_handles = list()

    # # Subplot 3.2
    # plt.subplot(2,1,2)
    # plot_skrifst_all()
    # plot_skrifst_kk()
    # plot_skrifst_kvk()
    # plt.title(', '.join(plot_title))
    # plt.legend(legend_handles, loc = 'upper left')
    # plot_title = list()
    # legend_handles = list()


    # # Figure 4
    # plt.figure()

    # # Subplot 4.1
    # plt.subplot(2,1,1)
    # plot_taeknar_all()
    # plot_taeknar_kk()
    # plot_taeknar_kvk()
    # plt.title(', '.join(plot_title))
    # plt.legend(legend_handles, loc = 'upper left')
    # plot_title = list()
    # legend_handles = list()

    # # Subplot 4.2
    # plt.subplot(2,1,2)
    # plot_verka_all()
    # plot_verka_kk()
    # plot_verka_kvk()
    # plt.title(', '.join(plot_title))
    # plt.legend(legend_handles, loc = 'upper left')
    # plot_title = list()
    # legend_handles = list()


    # # Figure 5
    # plt.figure()

    # plot_solu_all()
    # plot_solu_kk()
    # plot_solu_kvk()
    # plt.title(', '.join(plot_title))
    # plt.legend(legend_handles, loc = 'upper left')
    # plot_title = list()
    # legend_handles = list()

    # # Show plot
    # plt.show()
            
    # Print keys and relevant information
    # print()
    # print()
    # data.print_keys()
