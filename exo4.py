first_name = input("Quel est ton prénom?")

last_name = input("Quel est ton nom?")

adn = input("Quelle est ton année de naissance ?")

annee = float(2022)

print("Bienvenue " + first_name , last_name)



age = annee - float(adn)

print("Vu que tu es née en " + adn + ",je sais que tu as " + str(age) + " ans!")