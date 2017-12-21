from math import *
import argparse

def evalarg(text):
	return eval(text)
	
parser = argparse.ArgumentParser()
parser.add_argument('-s0', '--initial_position', type=evalarg,    # type=eval is also possible but won't have objects defined in namespace.
default=0.0, help="initial position", metavar='s0', dest='s0')
parser.add_argument('-v0', '--initial_velocity', type=float,
default=0.0, help="initial velocity", metavar='v0', dest='v0')
parser.add_argument('-a', '--acceleration', type=float,
default=1., help="acceleration", metavar='a', dest='a')
parser.add_argument('-t', '--time', type=float,
default=1.0, help="time", metavar='t', dest='t')
args = parser.parse_args()

s = args.s0 + args.v0*args.t + 0.5*args.a*args.t**2
print("s =", s)