#pour passer le variable A
import DiffieHellmanSharedSecretKey2 as s2


#pour proteger les donnees secrets de l'utilisateur
#puisque on va importer les script entre eux .
class privates:
	pass
private=privates()


p=int(raw_input("enter a prime integer (a big one) >> the same for both clients\n"))
g=int(raw_input("enter a prime integer (less then the first) >> the same for both clients\n"))


private.a=int(raw_input("choice a secret integer\n"))

A=pow(g,private.a)%p

Afile=open("A.DH","w")
Afile.write(str(A))
Afile.close()

raw_input("\nwaiting . . .")

Bfile=open("B.DH","r")
B=int(Bfile.read())
Bfile.close()

key=pow(B,private.a)%p

print ("your key is : ",key)

raw_input("\ntap to close . . .")

sys.exit()

