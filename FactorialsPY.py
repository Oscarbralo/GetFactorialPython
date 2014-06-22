class Factorial:
	def getFactorial(x):
		if x == 1:
			return x
		x *= getFactorial(x - 1)
		return x