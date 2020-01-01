#AoC 2019 - Level 5 - 1/1/2020 - Python
#reusing the code from level 2

import re

input = open('2019level5b.txt', 'r')
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
		ip1 = parse_parameter(numbers[positionnumber+1], paramip1)
        	ip2 = parse_parameter(numbers[positionnumber+2], paramip2)
        	output = numbers[positionnumber+3]
		print 'Addition:', ip1, '+', ip2, 'stored at position', output
		numbers[output] = ip1 + ip2
		print 'Result:', numbers[output]
		return positionnumber + 4

	#multiplication
	elif opcode == '02':
		ip1 = parse_parameter(numbers[positionnumber+1], paramip1)
        	ip2 = parse_parameter(numbers[positionnumber+2], paramip2)
        	output = numbers[positionnumber+3]
		print 'Mult:', ip1, '*', ip2, 'stored at position', output
		numbers[output] = ip1 * ip2
		print 'Result:', numbers[output]
		return positionnumber + 4

	#takes single int as input and saves it to the position given by its parameter
	elif opcode == '03':
		adress = numbers[positionnumber+1]
		userInput = raw_input('Expecting Input: ')
		userInput = int(userInput)
		print 'Storing', userInput, 'at adress', adress
		numbers[adress] = userInput
		return positionnumber + 2

	#outputs value of its only parameter
	elif opcode == '04':
		output = parse_parameter(numbers[positionnumber+1], paramip1)
		print 'Output is', output
		return positionnumber + 2

	#jump-if-true: if the first param is non-zero, it sets the ip to the value of the second param
	elif opcode == '05':
		ip1 = parse_parameter(numbers[positionnumber+1], paramip1)
		ip2 = parse_parameter(numbers[positionnumber+2], paramip2)
		if ip1 is not 0:
			print 'Jump-if-true: True. Jumping to', ip2
			return ip2
		else:
			print 'Jump-if-true: False. Not jumping'
			return positionnumber + 3

	#jump-if-false: if the first param is zero, it sets the ip to the value of the second param
	elif opcode == '06':
		ip1 = parse_parameter(numbers[positionnumber+1], paramip1)
                ip2 = parse_parameter(numbers[positionnumber+2], paramip2)
                if ip1 is 0:
			print 'Jump-if-false: True. Jumping to', ip2
                        return ip2
                else:
			print 'Jump-if-false: False. Not jumping'
                        return positionnumber + 3

	#less than: if the first param is less than the second, it stores 1 in the pos given by the
	#third param, otherwise it stores 0
	elif opcode == '07':
		ip1 = parse_parameter(numbers[positionnumber+1], paramip1)
                ip2 = parse_parameter(numbers[positionnumber+2], paramip2)
		output = numbers[positionnumber + 3]
                if ip1 < ip2:
			print 'Less than: True. Writing 1 in position', output
                        numbers[output] = 1
			return positionnumber + 4
                else:
			print 'Less than: False. Writing 0 in position', output
                        numbers[output] = 0
			return positionnumber + 4

	#equals: if the first param is equal to the second, it stores 1 in the pos given by the
	#third param, otherwise it stores 0
	elif opcode == '08':
		ip1 = parse_parameter(numbers[positionnumber+1], paramip1)
                ip2 = parse_parameter(numbers[positionnumber+2], paramip2)
                output = numbers[positionnumber + 3]
                if ip1 == ip2:
			print 'Equals: True. Writing 1 in position', output
                        numbers[output] = 1
                        return positionnumber + 4
                else:
			print 'Equals: False. Writing 0 in position', output
                        numbers[output] = 0
                        return positionnumber + 4

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
	position = newpos
