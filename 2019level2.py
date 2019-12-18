#AoC 2019 - Level 2 - 18/12/2019 - Python

import re

input = open('2019level2.txt', 'r')
numbers = re.findall('([0-9]+)', input.read())
state = 0
position = 0

class Code99Halt(Exception): pass

def sanitize(numbersarray):
	#convert strings into int before processing
	for i, number in enumerate(numbers):
		numbers[i] = int(number)

def process_opcode(opcode, positionnumber):

	#addition
	if opcode == 1:
		ip1 = numbers[positionnumber+1]
        	ip2 = numbers[positionnumber+2]
        	output = numbers[positionnumber+3]
		print 'Addition:', numbers[ip1], '+', numbers[ip2], 'stored at position', output
		numbers[output] = numbers[ip1] + numbers[ip2]
		print 'Result:', numbers[output]
		return 0

	#multiplication
	elif opcode == 2:
		ip1 = numbers[positionnumber+1]
        	ip2 = numbers[positionnumber+2]
        	output = numbers[positionnumber+3]
		print 'Mult:', numbers[ip1], '*', numbers[ip2], 'stored at position', output
		numbers[output] = numbers[ip1] * numbers[ip2]
		print 'Result:', numbers[output]
		return 0

	#exit opcode
	elif opcode == 99:
		print 'Exit triggered. Opcode 99'
		raise Code99Halt
		return 0

	#very primitive error handling
	else:
		print 'Code not recognized. Error'
		return 1

sanitize(numbers)

while True:
	try:
		process_opcode(numbers[position], position)
	except Code99Halt:
		break
	position = position + 4

print 'Value at 0 is:', numbers[0]
