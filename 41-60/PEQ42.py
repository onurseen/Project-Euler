with open('p042_words.txt', 'r') as text:
	text = text.read().replace('"', '').split(',')

def alphabetical(x):
	sum = 0

	for i in range(len(x)):
		sum += ord(x[i]) - 64 # A = 65, ...

	return sum

def control(x):
	temp = (((8 * alphabetical(x) + 1) ** 0.5) - 1) / 2
	
	if temp == int(temp):
		return True

	return False

def codedTriangleNumbers():
	counter = 0

	for i in range(len(text)):
		if control(text[i]):
			counter += 1
	
	return counter

print(codedTriangleNumbers())

