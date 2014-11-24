#tablademultiplicar

import sys 


print "parte 1"
M=int(sys.argv[1])
for i in range (1,21):
	R=i*M
	print str(i) + " * " + str(M) + " = " + str(R)
	
