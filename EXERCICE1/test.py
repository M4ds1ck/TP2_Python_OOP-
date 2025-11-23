from compte_bancaire import CompteBancaire

compte = CompteBancaire("Ali", 1000)
compte.deposer(200)
compte.retirer(150)

print(compte)
print("Solde accessible (lecture) :", compte.solde)
