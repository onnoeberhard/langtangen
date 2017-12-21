import sys
s = 0
for arg in sys.argv[1:]:
	number = float(arg)
	s += number
print("The sum of ", end="")
for arg in sys.argv[1:]:
	print(arg, end=" ")
print("is", s)
