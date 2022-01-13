while True:
           time = input("Donne moi un temps en seconde ")

           h, m = divmod(int(time),3600)

           s, ss =divmod(m,60)

           t, tt =divmod(ss,60)

           print("Voila ça fait " + str(h) + " heures, " + str(s) + " minutes et " + str(tt) + " secondes !")

           while True:
            answer = str(input('Recommencer (y/n): '))
            if answer in ('y', 'n'):
                break
            print("invalid input.")
            if answer == 'y':
                 continue
            else:
             print("Goodbye")
            break