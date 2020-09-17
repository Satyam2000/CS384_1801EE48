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
	gp=[]
	return gp 

# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n): 
	ap=[]
	return ap

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a, d, n): 
	hp=[]
	return hp

