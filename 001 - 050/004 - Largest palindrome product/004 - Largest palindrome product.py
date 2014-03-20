#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

number = 999
product = 1
pal = []

def testpal(product):
	if str(product) == (str(product)[::-1]):
		return(True)
	else:
		return(False)

while number > 99:
	i = 0
	
	for i in range(number):
		product = number * (number - i)
		if testpal(product) == True:
			pal.append(product)
			break
		i = i + 1

	number = number - 1

pal.sort()
print(str(pal[len(pal)-1]) + " is the largest palindrome.")