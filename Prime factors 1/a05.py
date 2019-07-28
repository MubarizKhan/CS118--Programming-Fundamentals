## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####

def is_prime(n):
 	if type(n) == float:
		n = int(n)

	if n < 2:
		return False


	for i in range(2, int((n**0.5) + 1)):
		if n % i == 0:
			return False
		else:
			return True

#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(x):
    
    for i in range(1, x +1):
        if x % i == 0:
            print i
            
            if x == i:
                break
#### End OF MARKER

#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####
def prime_for_largest(num):

	if num == 0 or num == 2 or num == 3 or num == 5 or num == 7:
		return num

	if num % num == 0 and num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
    	    return num
	else:
		return False


def get_largest_prime(num):

	if num < 2:
	    return None

	if type(num) == float:
	    num = int(num)

	list_prime = []

	if prime_for_largest(num):
	    list_prime.append(num)

	for h in range(1, num):
	    
	    if prime_for_largest(h):
	 	    list_prime.append(h)
	return max(list_prime)
	


#### End OF MARKER



if __name__ == '__main__':
    print is_prime(499)  # should return True

    print get_largest_prime(10)  # should return 7
    print get_largest_prime(100000)  # bonus, try with 100k

    output_factors(10)  # should output -- 1 2 5 10 -- one on each line
