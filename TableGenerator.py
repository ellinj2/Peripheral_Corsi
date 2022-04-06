from sys import argv
import random
import numpy

inputs = open("boxes.txt",'r').read()

if argv[-1] == 'n':
	filename = 'near.txt'
	text = inputs.split('# Blue')[-1]
	rows = [row for row in text.split('\n') if row != "# Second layer" and text]
	coords = []
	for line in rows:
		nums = line.split(' ')[2:4]
		if not nums:
			continue
		coords.append((nums[0], nums[1]))

if argv[-1] == 'm':
	filename = 'mid.txt'
	text = inputs.split('# Blue')[0].split("# Orange")[-1]
	rows = [row for row in text.split('\n') if row != "# Second layer" and text]
	coords = []
	for line in rows:
		nums = line.split(' ')[2:4]
		if not nums:
			continue
		coords.append((nums[0], nums[1]))

if argv[-1] == 'f':
	filename = 'far.txt'
	text = inputs.split('# Rose')[-1].split("# Orange")[0]
	rows = [row for row in text.strip().split('\n') if "Second layer" not in row]
	coords = []
	for line in rows:
		nums = line.split(' ')[2:4]
		if not nums:
			continue
		coords.append((nums[0], nums[1]))

max_path_size = 9
path_count = 100
with open(filename, 'w') as file:
	text = ''
	for i in range(path_count):
		path_size = random.randint(1, max_path_size)
		text += f"{path_size} "
		path = numpy.random.permutation(coords)[0:path_size]
		for coord in path:
			text += f"{coord[0]} {coord[1]} "
		for _ in range(max_path_size - path_size):
			text += "0 0 "
		text += '\n'

	text = text.strip()
	file.write(text)
