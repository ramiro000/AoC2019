#AoC 2019 - Level 5 - 1/1/2020 - Python
#reusing the code from level 2

import re

input = open('2019level5.txt', 'r')
#input = '1002,4,-33,1,99'
numbers = re.findall('(-?[0-9]+)', input.read())
state = 0
position = 0

class Code99Halt(Exception): pass

def sanitize(numbersarray):
	#convert strings into int before processing
	for i, number in enumerate(numbers):
		numbers[i] = int(number)

def parse_param_mode(opcode, positionnumber):
	#parses all the parameters from the opcode
	opcode = map(int, str(opcode))
	if len(opcode) is not 5:
		while len(opcode) is not 5:
			opcode.insert(0, 0)
	opcodenumber = str(opcode[3]) + str(opcode[4])
	print 'Opcode Number is:', opcodenumber
	paramip1 = opcode[2]
	paramip2 = opcode[1]
	return opcodenumber, paramip1, paramip2

def parse_parameter(parameter, mode):
	#parses each indivual parameter with its mode and returns the expected parameter
	#position mode
	if mode == 0:
		return numbers[parameter]

	#immediate mode
	elif mode == 1:
		return parameter

	else:
		print 'Error, unrecognized mode' + mode
		return -1

def process_opcode(opcode, paramip1, paramip2, positionnumber):

	#addition
	if opcode == '01':
		ip1 = numbers[positionnumber+1]
        	ip2 = numbers[positionnumber+2]
        	output = numbers[positionnumber+3]
		print 'Addition:', parse_parameter(ip1, paramip1), '+', parse_parameter(ip2, paramip2), 'stored at position', output
		numbers[output] = parse_parameter(ip1, paramip1) + parse_parameter(ip2, paramip2)
		print 'Result:', numbers[output]
		return 4

	#multiplication
	elif opcode == '02':
		ip1 = numbers[positionnumber+1]
        	ip2 = numbers[positionnumber+2]
        	output = numbers[positionnumber+3]
		print 'Mult:', parse_parameter(ip1, paramip1), '*', parse_parameter(ip2, paramip2), 'stored at position', output
		numbers[output] = parse_parameter(ip1, paramip1) * parse_parameter(ip2, paramip2)
		print 'Result:', numbers[output]
		return 4

	#takes single int as input and saves it to the position given by its parameter
	elif opcode == '03':
		adress = numbers[positionnumber+1]
		userInput = raw_input('Expecting Input: ')
		userInput = int(userInput)
		print 'Storing', userInput, 'at adress', adress
		numbers[adress] = userInput
		return 2

	#outputs value of its only parameter
	elif opcode == '04':
		output = numbers[positionnumber+1]
		print 'Output is', parse_parameter(output, paramip1)
		return 2

	#exit opcode
	elif opcode == '99':
		print 'Exit triggered. Opcode 99'
		raise Code99Halt
		return 0

	#very primitive error handling
	else:
		print 'Code not recognized. Error' + opcode
		return 0

sanitize(numbers)

while True:
	try:
		opcode, paramip1, paramip2 = parse_param_mode(numbers[position], position)
		newpos = process_opcode(opcode, paramip1, paramip2, position)
	except Code99Halt:
		break
	position = position + newpos
