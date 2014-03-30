#The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

#How many n-digit positive integers exist which are also an nth power?

results = set()

for base in range(1, 10):
	for expo in range(1, 22):
		number = base**expo
		if len(str(number)) == expo:
			results.add(number)
			print number, base, expo
		if len(str(number)) >> expo: break

print len(results)