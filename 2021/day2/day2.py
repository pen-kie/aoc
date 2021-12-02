file = open('inputDay2.txt', 'r')
course = file.readlines()


# part1
def calculateCourse():
	horizontal = 0
	depth = 0
	for move in course:
		move = move.strip().split()
		direction = move[0]
		extent = move[1]
		if direction == 'forward':
			horizontal = horizontal + int(extent)
		elif direction == 'down':
			depth = depth + int(extent)
		else:
			depth = depth - int(extent)

	print(horizontal * depth)


# part2
def calculateRightCourse():
	horizontal = 0
	depth = 0
	aim = 0
	for move in course:
		move = move.strip().split()
		direction = move[0]
		extent = move[1]
		if direction == 'forward':
			horizontal = horizontal + int(extent)
			depth = depth + (aim * int(extent))
		elif direction == 'down':
			aim = aim + int(extent)
		else:
			aim = aim - int(extent)

	print(horizontal * depth)