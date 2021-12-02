
file = open('inputDay1.txt', 'r')
lines = file.readlines()

def measureDepth():
	prev_num = None
	increased = 0
	for index, number in enumerate(lines):
		number = number.strip()
		if number.isdigit():
			number = int(number)
			if index != 0 and number > prev_num:
				increased = increased+1
			prev_num = number
	print(increased)



def compareWindows():
	increase = 0
	digitList = [line.strip() for line in lines if (line.strip().isdigit())]
	for i in range(len(digitList)):
		if (i + 3) < len(digitList):
			if(int(digitList[i]) + int(digitList[i+1]) + int(digitList[i+2]) < int(digitList[i+1]) + int(digitList[i+2]) + int(digitList[i+3])):
				increase = increase+1
	print(increase)
