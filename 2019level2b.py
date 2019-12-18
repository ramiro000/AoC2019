#AoC 2019 - Level 2 - 18/12/2019 - Python

import re

input = open('2019level2.txt', 'r')
numbers_original = re.findall('([0-9]+)', input.read())
numbers = []
position = 0

class Code99Halt(Exception): pass

def sanitize(numbersarray):
	#convert strings into int before processing
	for i, number in enumerate(numbers_original):
		numbers_original[i] = int(number)

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

def process_program(value1, value2, numbersarray):
	numbersarray[1] = value1
	numbersarray[2] = value2
	global position
	while True:
		try:
			process_opcode(numbersarray[position], position)
		except Code99Halt:
			break
		position = position + 4
	return 0

sanitize(numbers_original)
numbers = list(numbers_original)
for v1 in range(100):
	for v2 in range(100):
		process_program(v1, v2, numbers)
		if numbers[0] == 19690720:
			print 'Found!:', v1, '+', v2, '=', '19690720'
			break
		else:
			print 'No match with', v1, 'and', v2, ' Resetting...'
			position = 0
			numbers = list(numbers_original)

	if numbers[0] == 19690720:
		break
