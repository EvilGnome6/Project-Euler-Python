#A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

#The text file, keylog.txt, contains fifty successful login attempts.

#Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

attempts = []
file = open('keylog.txt')
for i in range(50):
	attempts.append(int(file.readline()))

#collect which digits the code is composed of
digits = []
for d in range(10):
	for a in attempts:
		if str(d) in str(a):
			digits.append(d)
			break

#sort the digits to match the passcode attempts:

for a in attempts:
	astring = str(a)
	d1 = int(astring[0])
	d2 = int(astring[1])
	d3 = int(astring[2])
	if digits.index(d1) > digits.index(d2):
		a, b = digits.index(d1), digits.index(d2)
		digits[a], digits[b] = digits[b], digits[a]
	if digits.index(d2) > digits.index(d3):
		a, b = digits.index(d2), digits.index(d3)
		digits[a], digits[b] = digits[b], digits[a]

passcode = ''

for d in digits:
	passcode += str(d)

print passcode
