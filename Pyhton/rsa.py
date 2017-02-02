import time
#********computes the value of n and phi(n)*************
def product_n(p,q):
	product=p*q  
	return product
def totient_n(p,q):
	totient=(p-1)*(q-1)
	return totient
#*******checks if the number is prime or not************
def is_prime(prime_test):
	return all(prime_test % b for b in range(2, prime_test))	
#******checks if the numbers are co_prime***************
def co_prime_check(e_intest,phi,min_test):
	for c in range(2,min_test + 1):
		if(e_intest%c==0):
			if(phi%c==0):
				return 0
	if(c== min_test):
		return 1
#*****displays the generated keys***********************
def print_values(p,q,n_forCalculation,phi,calculated_e,k,calculated_d):
	print("p= ",p,"q= ",q,"n= ",n_forCalculation,"phi= ",phi,"e= ",calculated_e,"k= ",k,"d= ",calculated_d)	
	to_print="p="+str(p)+"  "+"q="+str(q)+"  "+"n="+str(n_forCalculation)+"  "+"phi="+str(phi)+"  "+"e="+str(calculated_e)+"  "+"k="+str(k)+"  "+"d="+str(calculated_d)+"\n"
	text_file.write(to_print)
#**********computation of d and e***********************
def e_d_value(default,default1,p,q,n_forCalculation,phi,justforloop):
	if(p>=50):
		for prime_check in range(3,q,2):
			is_prime_true=is_prime(prime_check)
			if(is_prime_true):
				e_intest=prime_check
				if(e_intest>phi):
					min_test=phi
				else:
					min_test=e_intest
				is_coprime_true=co_prime_check(e_intest,phi,min_test)
				if(is_coprime_true==1):
					if((2**e_intest)>n_forCalculation):
						calculated_e=e_intest
						default=value_d(default1,calculated_e,phi,p,q,n_forCalculation,justforloop)
	else:
		for prime_check in range(3,n_forCalculation,2):
			is_prime_true=is_prime(prime_check)
			if(is_prime_true):
				e_intest=prime_check
				if(e_intest>phi):
					min_test=phi
				else:
					min_test=e_intest
				is_coprime_true=co_prime_check(e_intest,phi,min_test)
				if(is_coprime_true==1):
					if((2**e_intest)>n_forCalculation):
						calculated_e=e_intest
						default=value_d(default1,calculated_e,phi,p,q,n_forCalculation,justforloop)
	return default
def value_d(default1,calculated_e,phi,p,q,n_forCalculation,justforloop):
	for k in range(1,30):
		if(justforloop==0):
			calculating_d=int((1+(k*phi))/calculated_e)
			if(((calculating_d*calculated_e)%phi)==1):	
				justforloop=justforloop+1
				calculated_d=calculating_d
				default1.append(n_forCalculation)
				default1.append(calculated_e)
				default1.append(calculated_d)
				print_values(p,q,n_forCalculation,phi,calculated_e,k,calculated_d)
	return default1;
#***************************************************************#
def get_input_as_list(input):
	f = open(input,'r')
	arrayList = []
	for line in f.readlines():
	    arrayList.extend(line.split())
	f.close()
	return arrayList
#***********Main program starts here*************************#
text_file=open("keys_generated.txt","w")
text_file2=open("message_enryptedValue.txt","w")
text_file.write("\t\t\t\t\t\t\t\tRSA Key Generation:\n")
text_file2.write("\t\t\t\t\t\t\tMessage and Encrypted Value:\n")																	
#generate random prime number in the given range
print("Enter the range you want to generate your prime numbers in \n")
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
start_time=time.clock()
primes=[]
default=[]
default1=[]
default_e=0
default_d=0
default_n=0
e_d=[]
if(lower==0):
	lower=3
for i in range(lower,upper):
	if is_prime(i):			
		primes.append(i)
print("prime numbers generated are:",primes)
for j in range(0,len(primes)):
	for w in range(1,len(primes)):
		if(primes[j]==primes[w]):
			break
		p=primes[j]
		q=primes[w]
		n_forCalculation=product_n(p,q)
		phi=totient_n(p,q)
		justforloop=0
		e_d=e_d_value(default,default1,p,q,n_forCalculation,phi,justforloop)
#print("l is:",len(e_d))
default_n=e_d[len(e_d)-3]
default_e=e_d[len(e_d)-2]
default_d=e_d[len(e_d)-1]
text_file.close()
print("--- %s seconds ---" % (time.clock() - start_time))
input_y_n=int(input("Do you have an input file.\nIf yes press 1 or else press 0:\n "))
while(input_y_n!=0 | input_y_n!=1):
	print("Enter an appropriate integer \n")
	input_y_n=int(input("Do you want to give the input from the file ?.\n If yes press 1 or else press 0:\n "))
input_n= int(input("Enter the value of n:\n "))
if(input_n==0):
	input_n=default_n
	input_e=default_e
	input_d=default_d
	print("n=",input_n,"  ","e=",input_e,"  ","d=",input_d,"\n")
else:
	input_e =int(input("Enter the value of e :\n "))	
	input_d= int(input("Enter the value of d:\n "))
returnedlist=[]
if(input_y_n==1):
	input=input("Please enter the filelocation:\n")
	returnedlist=get_input_as_list(input)
	for i in returnedlist:
		y=int(i)
		if((y!=((input_n)-1)) & (y<((input_n)-1))):
			input_integer=y
			if(input_integer!=0):
				encrypted_value=((input_integer**input_e)%input_n)
				decrypted_value=((encrypted_value**input_d)%input_n)
				print("input num:",input_integer,"\t encrypted value is:",encrypted_value,"\t decrypted value is:",decrypted_value)
				m_e="message="+str(input_integer)+"  "+"encrypted_value="+str(encrypted_value)+"\n"
				text_file2.write(m_e)
			else:
				break
else:
	input_integer =int(input("Enter interger to be encrypted:\n "))
	while(input_integer!=0):
		while(input_integer>=((input_n)-1)):
			print("Enter an integer less than n-1\n")
			input_integer =int(input("Enter integer to be encrypted:\n "))
		if(input_integer!=0):
			encrypted_value=((input_integer**input_e)%input_n)
			decrypted_value=((encrypted_value**input_d)%input_n)
			print("input num:",input_integer,"\t encrypted value is:",encrypted_value,"\t decrypted value is:",decrypted_value)
			m_e="message="+str(input_integer)+"  "+"encrypted_value="+str(encrypted_value)+"\n"
			text_file2.write(m_e)
			input_integer =int(input("Enter integer to be encrypted:\n "))
text_file2.close()

