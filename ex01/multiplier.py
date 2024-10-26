def multiplier(a, b):

	result = 0

	while b > 0:

		# If the number is odd, add the value of a to the result
		if b & 1:
			result = result + a

		# Double the value of a and halve the value of b
		a = a << 1
		b = b >> 1

	return result


#Russian peasant multiplication
#In the Russian peasant method, the powers of two in the decomposition of the multiplicand
# are found by writing it on the left and progressively halving the left column, discarding any remainder,
# until the value is 1 (or −1, in which case the eventual sum is negated), while doubling the right column as before.
#Lines with even numbers on the left column are struck out, and the remaining numbers on the right are added together.[3]
