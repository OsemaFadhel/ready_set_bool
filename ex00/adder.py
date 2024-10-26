def adder(a, b):

	while b != 0:
		carry = a & b; # carry value
		a = a ^ b; # sum of bits of a and b
		b = carry << 1; # carry is shifted by one so that adding it to a gives the required sum

	return a;

#The whole idea behind this code is that the carry gets added again with the sum value.
# So what we do is we find the value of the carry separately using the expression a & b
# and use it again to find the sum. We keep on doing this till the carry value becomes 0.
#Another important point to note here is that we shift the carry towards the left by 1 bit.
# That's because the carry value is added to the next bit rather than the current bit.
#We keep on repeating this process till the carry value i.e. a & b becomes 0 .
# And finally, we get the required sum of the two numbers.

# https://iq.opengenus.org/addition-using-bitwise-operations/
