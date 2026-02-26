import sys
##programme de la calculatrice

def additionne (a,b):
	return a+b
	
def multiplie (a,b):
	resultat = 0
	for i in range (abs(b)):
		resultat = resultat +a
	if b<0 : 
		return -resultat
	return resultat

def divise (a,b):
	return a/b

def soustrait (a,b):
	return a-b

########################################
############## interaction #############
########################################

terme_gauche = float(sys.argv[1])
operande = sys.argv[2]
terme_droite = float(sys.argv[3])

if operande == "+":
	print(additionne(terme_gauche,terme_droite))
elif operande == "*":
	print(multiplie(terme_gauche,terme_droite))
elif operande == "/":
	print(divise(terme_gauche,terme_droite))
elif operande == "-":
	print(soustrait(terme_gauche,terme_droite))
else : 
	print("l'opérande n'est pas valide")
