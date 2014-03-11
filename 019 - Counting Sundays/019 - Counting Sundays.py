#You are given the following information, but you may prefer to do some research for yourself.

#    1 Jan 1900 was a Monday.
#    Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

wday = "Tue"
count = 0

for year in range(1901, 2001, 1):
	leap = False
	if (year %4 == 0): leap = True
	for month in range(1, 13, 1):
		if (month == 2 and leap == False): days = 28
		elif (month == 2 and leap == True): days = 29
		elif (month == 4 or month == 6 or month == 9 or month == 11): days = 30
		else: days = 31
		for day in range(1, days+1, 1):
			if (wday == "Sun" and day == 1):
				count = count + 1
				print(str(year) + "/" + str(month) + "/" + str(day) + " " + wday + " (" + str(count) + ")")
			if (wday == "Mon"): wday = "Tue"
			elif (wday == "Tue"): wday = "Wed"
			elif (wday == "Wed"): wday = "Thu"
			elif (wday == "Thu"): wday = "Fri"
			elif (wday == "Fri"): wday = "Sat"
			elif (wday == "Sat"): wday = "Sun"
			else: wday = "Mon"


