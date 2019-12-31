#AoC 2019 level 4 - 18/12/2019 - Python - Part 1 was done, but I abandoned it midway Part 2, will
#look for a cleaner solution overall

import re

def password_criteria_count(range, range2):
	matchescount = 0
	matchesvalue = [0]
	x = xrange(range, range2)
	for i in x:
		digits = [int(d) for d in str(i)]
		lastdigit = ''
		penultimatedigit = ''
		for digit in digits:
			if lastdigit == '':
				lastdigit = digit
			elif lastdigit == digit and penultimatedigit != digit:
				if matchesvalue[-1] == i:
					penultimatedigit = lastdigit
					lastdigit = digit
					continue
				else:
					matchescount += 1
					matchesvalue.append(i)
					penultimatedigit = lastdigit
					lastdigit = digit
			elif penultimatedigit == digit:
				if matchesvalue[-1] == i:
					matchesvalue.pop()
					matchescount -= 1
					break
				break
			elif int(digit) < int(lastdigit):
				if matchesvalue[-1] == i:
					matchesvalue.pop()
					matchescount -= 1
					penultimatedigit = lastdigit
					lastdigit = digit
					break
				break
			else:
				penultimatedigit = lastdigit
				lastdigit = digit

	return matchescount, matchesvalue

count, values = password_criteria_count(183564, 657474)
print "Number of different passwords matching the criteria: ", count
print values
