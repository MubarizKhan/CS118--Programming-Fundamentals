## IMPORTS GO HERE

## END OF IMPORTS 
from math import pi

#### YOUR CODE FOR get_area GOES HERE ####
def get_area(radius):
	a= pi * radius**2
        return a

#### End OF MARKER


#### YOUR CODE FOR output_parameter GOES HERE ####
def output_parameter(radius):
    c = 2 * pi * radius
    return c

#### End OF MARKER  




if __name__ == '__main__': 
    print get_area(2) 
    output_parameter(1.0) 

