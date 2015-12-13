import random

inputString = raw_input('Enter phrase: ')
inputList = inputString.split()
outputList = []

for word in inputList:
	if len(word) > 3:
		midWord = list(word[1:-1])
		random.shuffle(midWord)
		outputList.append(word[0] + ''.join(midWord) + word[-1])
	else:
		outputList.append(word)
		

print ' '.join(outputList)

