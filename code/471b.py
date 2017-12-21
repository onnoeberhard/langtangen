import sys

try:
    C = float(sys.argv[1])
except IndexError:
    print("You did not provide a Celsius value in the command line!")
    sys.exit(1)
except ValueError:
    print("The temperature in Celsius must be numeric!")
    sys.exit(1)

F = 9/5*C + 32
print("%g°C = %g°F" % (C, F))
