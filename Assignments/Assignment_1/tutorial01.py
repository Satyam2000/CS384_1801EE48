# Function to add two numbers 
def add(num1, num2): 

	if(not isinstance(num1,int)) and (not isinstance(num2,int)) :
		return  0

	else:
		addition = num1 + num2
		return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
	if(not isinstance(num1,int)) and (not isinstance(num2,int)) :
		return  0

	else :
		subtraction = num1 - num2
		return subtraction

# Function to multiply two numbers 
def multiply(num1, num2): 
	#Multiplication Logic 

	if(not isinstance(num1,int)) and (not isinstance(num2,int)) :
		return  0
	
	else:
		multiplication = num1 * num2
		return multiplication

# Function to divide two numbers 
def divide(num1, num2): 
	#DivisionLogic 
	if(not isinstance(num1,int)) and (not isinstance(num2,int)) :
		return  0
	
	elif (num2==0):
		return 0

	else:	
		division = num1/num2
		return division
		
# Function to add power function
#You cant use the inbuilt python function x ** y . Write your own function
def power(base, exp): #base ^ exp
	#Power Logic 
	if(not isinstance(exp,int)):
		return 0

	elif(not isinstance(base,float)) and (not isinstance(base,int)) :
		return  0

	elif(base==0):
		return 0	

	elif (base==1):
		return 1

	elif (exp==0) :
		return 1
	
	elif (base!=0) and (exp<0):
		return  round(1/power(base, -exp),3)

	elif(exp==1):
		return(base)
	
	if(exp!=1) :
		return round((base * power(base, exp-1)), 3)

	
# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function
def printGP(a, r, n): 
	if(not isinstance(n,int)):
		return [0]

	elif(not isinstance(r,int)) and (not isinstance(r,float)) :
		return [0]

	if(not isinstance(a,int)) and (not isinstance(a,float)) :
		return [0]

	gp=[]
	for i in range(0,n):
		gp.append(a*power(r,i)) 
	return gp 

# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n):
	if(not isinstance(n,int)):
		return [0] 
	ap=[]
	for i in range(0,n):
		ap.append(a+(i*d))
	return ap

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a, d, n): 
	hp=[]
	if(not isinstance(n,int)):
		return hp

	if(not isinstance(a,int)) and (not isinstance(a,float)) :
		return hp

	if(not isinstance(d,int)) and (not isinstance(d,float)) :
		return hp
		
	ap=printAP(a,d,n)
	for i in range(0,n):
		if(ap[i]==0):
			hp.append(round(0,3))
		else:
			hp.append(round(1/ap[i],3))
	return hp