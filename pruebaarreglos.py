print "Parte 1"

A=[0,0,0,0,0,0,0,0]
B=[0,0,0,0,0,0,0,0]

A[5]=7
A[3]=8
A[0]=4
A[7]=2
A[6]=8
A[2]=3
A[1]=1
A[4]=9

print A

#####################################
print "Parte 2"

B[0]=A[0]
B[1]=A[1]
B[2]=A[2]
B[3]=A[3]
B[4]=A[4]
B[5]=A[5]
B[6]=A[6]
B[7]=A[7]

print B

#####################################
print "Parte 3"

C=[1,1,1,1,1,1,1,1] 
print C

for i in [0,1,2,3,4,5,6,7]:
	
	print i
	
	C[i]=B[i]
	
print C
#####################################
print "parte 4"

D=[1,1,1,1,1,1,1,1]
print D

for i in [0,1,2,3,4,5,6,7]:
	
	print i
	
	D[i]=C[i]*2

print D








	
	
