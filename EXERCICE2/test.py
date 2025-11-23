from client_compte import Client

cli = Client("Yassir")
cli.compte.deposer(300)
cli.compte.retirer(50)
cli.afficher()
