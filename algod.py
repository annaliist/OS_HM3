from tkinter import messagebox
    
järjend = [[['A', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
['A', 'A', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'D', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
['A', 'A', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'D', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
['A', 'A', 'E', 'E', 'E', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
['A', 'A', 'E', 'E', 'E', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', 'E', 'E', 'E', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
['A', 'A', 'E', 'E', 'E', 'C', 'C', 'C', 'C', 'E', 'E', 'E', ' ', ' ', 'E', 'E', 'E', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
['A', 'A', 'E', 'E', 'E', 'C', 'C', 'C', 'C', 'E', 'E', 'E', 'F', 'F', 'E', 'E', 'E', 'E', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']], 4, 5]

def kaivita(jarjend):
    valjund = [[]]
    fragmenteerunud_failid = []
    failid = []
    fragmenteerunud_ruum = 0
    lisatavad_plokid = 0
    i = 0

    # täidame lõpp-järjendi tühjade väljadega
    for k in range(len(jarjend)):
        valjund[0].append([])
        for s in range(48):
            valjund[0][k].append(" ")

    # [['A', 2], ['B', 3], ['A', 0], ['C', 4], ['B', '+', 3], ['D', 5], ['E', 15], ['C', 0], ['F', 5]]
    for samm in jarjend:
        #print("SAMM " + str(i+1))

        if i > 0: # kopeerime eelneva sammu, et seda modifitseerida
            valjund[0][i] = list(valjund[0][i - 1])


        if len(samm) > 2: # plokke lisatakse juba olemasolevale failile
                #print("lisame faili " + samm[0] + " plokke")
                lisatavad_plokid = samm[2]

                for plokk in range(len(valjund[0][i])):
                    if valjund[0][i][plokk] == " ":
                        valjund[0][i][plokk] = samm[0]
                        lisatavad_plokid -= 1

                    if lisatavad_plokid == 0:
                        break
        else:
            if samm[1] == 0: # fail kustutatakse
                #print("kustutame faili " + samm[0])
                
                for plokk in range(len(valjund[0][i])):
                    if valjund[0][i][plokk] == samm[0]:
                        valjund[0][i][plokk] = " "
            else: # fail luuakse
                #print("loome faili " + samm[0])
                lisatavad_plokid = samm[1]

                for plokk in range(len(valjund[0][i])):
                    if valjund[0][i][plokk] == " ":
                        valjund[0][i][plokk] = samm[0]
                        lisatavad_plokid -= 1

                    if lisatavad_plokid == 0:
                        break
        
        if lisatavad_plokid != 0: # lisatav fail ei mahu
            messagebox.showerror(title="Fail ei mahu", message="Sammu " + str(i+1) + " jooksul lisatav fail " + str(samm[0]) + " ei mahu!" + "\n" + "Fragmenteerumist ei arvutata.")
            valjund.append(0) # allesjäänud failide fragmenteerumist ei arvutata
            valjund.append(0) # kasutatud ruumi fragmenteerumise protsenti ei arvutata
            return valjund
        
        #print(valjund[0][i])
        i += 1
        
    # otsin fragmenteerunud faile
    i = 0
    kasutatud = 0
    for plokk in valjund[0][-1]: # vaatame viimase sammu tulemust
        if plokk != " ":
            kasutatud += 1

            if plokk not in failid:
                failid.append(plokk)
    
    viimane = list(valjund[0][-1])
    fragmenteerunud = []
    for plokk in range(len(viimane)):
        try:
            if viimane[plokk] != viimane[plokk + 1]:
                fragmenteerunud.append(viimane[plokk])
        except:
            if viimane[plokk] != viimane[plokk - 1]:
                fragmenteerunud.append(viimane[plokk])
    
    for z in fragmenteerunud:
        if z == " ":
            fragmenteerunud.remove(z)

    for fail in failid:
        if fragmenteerunud.count(fail) > 1:
            fragmenteerunud_failid.append(fail)

    # arvutan fragmenteerunud failidele kuuluvat ala
    for f in fragmenteerunud_failid:
        for plokk in viimane:
            if f == plokk:
                fragmenteerunud_ruum += 1

    fragmenteerunute_protsent = round(len(fragmenteerunud_failid) / len(failid) * 100, 2)
    fragmenteerunud_ruum = round(fragmenteerunud_ruum / kasutatud * 100, 2)

    valjund.append(fragmenteerunute_protsent)
    valjund.append(fragmenteerunud_ruum)
    return valjund


