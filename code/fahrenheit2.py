import sys
try:
    F = float(sys.argv[1])
except IndexError as e:
    raise IndexError("You have to specify the temperature in Fahrenheit as a command line argument.")
print("The temperature in Celsius is: %g" % (5/9 * (F - 32)))
