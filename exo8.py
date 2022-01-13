print("Hello mon garçon. 😎")
grades_number = input("Combien veux-tu calculer de note(s)? ") 

print("D'accord. Super. Génial. Ma gueule. 😋")
print("Entre moi " + grades_number +" notes, de 0 à 20 s'il te plait. Et je te rends la moyenne!")

print()

# Liste de notes
grades = []

# range(max) > range(5) > 0 ... 4
# range(min, max) > range(1, 5) > 1 ... 4
for i in range(int(grades_number)) :
    # Demande la  note à l'utilisateur
    grade = int(input("Entre la note n°" + str(i + 1) + ": "))

    while (grade > 20) or (grade < 0):
        print("Ta note n'est pas valide! Réessaye. 🥱")
        grade = int(input("Entre la note n°" + str(i + 1) + ": "))

    # Ajoute la note à la liste
    grades.append(grade)

grades_sum = 0

# Calcule la somme des notes
for grade in grades :
    grades_sum = grades_sum + grade

# Calcule la moyenne
average = grades_sum / int(grades_number)

print("La moyenne vaut " + str(average))