#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

numeprod = 1
denoprod = 1

for deno in range(10, 100):
	for nume in range(10,100):
		if nume/deno > 1: break
		 
		nume1 = int(str(nume)[0])
		nume2 = int(str(nume)[1])
		
		deno1 = int(str(deno)[0])
		deno2 = int(str(deno)[1])
		
		if nume1 != 0 and nume2 != 0 and deno1 != 0 and deno2 != 0 and nume != deno:
			if nume1 == deno2:
				if nume2/float(deno1) == nume/float(deno): 
					print(nume, deno, nume2/float(deno1))
					numeprod *= nume
					denoprod *= deno
			if nume2 == deno1:
				if nume1/float(deno2) == nume/float(deno): 
					print(nume, deno, nume1/float(deno2))
					numeprod *= nume
					denoprod *= deno

print(numeprod, denoprod)
print(denoprod/numeprod)
