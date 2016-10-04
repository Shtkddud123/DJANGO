import sys
import compute 

def get_input():
    """Get input from the input line"""
    r = float(sys.argv[1])
    return r 

def present_output(r):
    """Write results to terminal window"""
    s = compute.compute(r)
    print "Hello, World! sin(%g) = %g" % (r,s)
