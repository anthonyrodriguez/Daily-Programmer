import sys
import pdb

def threeRecurse(num, stepList):
	if num == 1:
		if sum([x[1] for x in stepList]) == 0:
			for item in stepList:
				print "{0} {1}".format(item[0], item[1])
			print "1"
			#print "sum: {}".format(sum([x[1] for x in stepList]))
			return True
		return False

	if num < 1:
		return False

	if num % 3 == 0:
		if threeRecurse(num / 3, stepList + [(num, 0)]):
			return True
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

if not threeRecurse(start, []):
	print "Impossible."


