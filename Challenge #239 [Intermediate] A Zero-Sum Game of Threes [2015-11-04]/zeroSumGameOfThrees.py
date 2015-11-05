import sys

def threeRecurse(num, stepList):
	if num == 1 and sum([x[1] for x in stepList]) == 0:
		for item in stepList:
			print "{0} {1}".format(item[0], item[1])
		return True

	if num % 3 == 0:
		return threeRecurse(num / 3, stepList + [(num, 0)])
	if (num + 1) % 3 == 0:
		if threeRecurse( (num + 1) / 3, stepList + [(num, 1)]):
			return True
		if threeRecurse( (num - 2) / 3, stepList + [(num, -2)]):
			return True
	if (num - 1) % 3 == 0:
		if threeRecurse( (num - 1) / 3, stepList + [(num, -1)]):
			return True
		if threeRecurse( (num + 2) / 3, stepList + [(num, 2)]):
			return True
	return False

try:
	start = int(sys.argv[1])
	if start < 1:
		raise ValueError('Argument must be greater than zero!')
except:
	raise TypeError('Argument should be a positive integer!')

if !threeRecurse(start, []):
	print "Impossible."

