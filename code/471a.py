import sys

try:
    C = float(sys.argv[1])
except:
    print("You did not provide a Celsius value in the command line!")
    sys.exit(1)

F = 9/5*C + 32
print("%g°C = %g°F" % (C, F))
