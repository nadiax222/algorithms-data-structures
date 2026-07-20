# Write a program that swaps two variables without using a third variable (max. 1)
# Program

# PSEUDOCODE:
# Operators used in the program should be defined at the beginning of the file with pseudocode as follows:
# // a SHIFTL b – operator that shifts the binary representation of number a to the left by b bits, drops bits from the left, and appends zeros on the right
# Also provide the priority table of operators used in pseudocode.
# // OPERATOR PRIORITY
#		//	()
#		//	+ -
#		//	SHIFTL
#		//	=
# A line starting with // indicates a comment in pseudocode to the end of the line.
# Also specify the number of operations in your solution.
#		int a, b, x
#		a = 2
#		b = 3
#		write(a,b) // output variable values
#       x = a    // 1 assignment
#		a = b    // 1 assignment
#		b = x    // 1 assignment
#		// total 3 operations
#		write(a,b) // output variable values

A = 2
B = 3
print("before change: A =", A, "B =", B)

A = A + B
B = A - B
A = A - B

print("after change: A =", A, "B =", B)


