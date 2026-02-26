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