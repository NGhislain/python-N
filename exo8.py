valeur=[0,0,0,0,0]

#prise des notes et écritures dans la variable
for i in range(5) :
    u=i
    list = i+1
    valeur[int(i)] = input("entre la note "+str(i+1)+":")

    if int(valeur[i])>int(20) :
        valeur[i]=0
        u=i
        print("Recommence et utilese un nombre entre 0 et 20")
        valeur[int(i)] = input("entre la note "+str(i)+":")


print(valeur)


#calcul de la moyenne 
note =str((int(valeur[0])+int(valeur[1])+int(valeur[2])+int(valeur[3])+int(valeur[4]))/int(5))
print(str(note)+"/20")


#afficher une remarque par rapport aux points
if float(note) <= float(4) :
    print("pas terrible.")
elif float(note) <= float(9) :
    print("pas au top. Motivez-vous les gars.")
elif float(note) <= float(14) :
    print("bonne! Continuez comme ça.")
elif float(note) <= float(19) :
    print("au top! Vous êtes les meilleurs.")
else :
    print("INSANE! Prenez ma place.")