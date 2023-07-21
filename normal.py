import random


maj = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lettres = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["1","2","3","4","5","6","7","8","9"]
special = ["ù","$","*","µ","%","!","§",":","/","¨","^","<",">",";","."]


caracteres = lettres + numbers + special + maj

passwords = input("Combien de mot de passes je dois générer ? ")
passwords_length = input("Combien voulez vous que vos mot de passe on de caractères ? ")

try:
    numbers_password = 0
    for i in range(0, int(passwords)):
        mdp = ""
        numbers_password += 1
        for i in range(0, int(passwords_length)):
            cmdp = random.choice(caracteres)
            mdp = mdp + cmdp
        
        print(f"Mot de passe {numbers_password}: {mdp}")
    
    
except Exception as e:
    print("Erreur;")
    print(e)