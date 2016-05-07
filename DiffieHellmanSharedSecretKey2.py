#pour passer le variable A
import DiffieHellmanSharedSecretKey1 as s1
import sys

#pour proteger les donnees secrets de l'utilisateur
#puisque on va importer les script entre eux .
class privates:
	pass
private=privates()


#choix des variables de base

p=int(raw_input("enter a prime integer (a big one) >> the same for both clients\n"))
g=int(raw_input("enter a prime integer (less then the first) >> the same for both clients\n"))

#entier secret
private.b=int(raw_input("choice a secret integer\n"))

B=pow(g,private.b)%p

#j'ai utiliser les fichier pour transmettre A et B entre les 2 clients

Bfile=open("B.DH","w")
Bfile.write(str(B))
Bfile.close()
raw_input("\nwaiting . . .")

Afile=open("A.DH","r")
A=int(Afile.read())
Afile.close()

key=pow(A,private.b)%p

print ("your key is : ",key)

raw_input("\ntap to close . . .")

sys.exit()