
primero=103
n=437
anterior=56
x=1

print "n"
print n
print "primero:"
print primero
print "anterior"
print anterior
print "x"
print x


if x==0:
	print "es igual a 0"
	resultado=(anterior*anterior)%n
elif x==1:
	print "es igual a 1"
	resultado=(anterior*anterior*primero)%n
print "resultado"
print resultado

