
def output_prime_factors(prime):
    if type(prime) == float:
       
        prime = int(round(prime))
   

    factors_of_prime = []
    
    for i in range(1, prime + 1):
        

        if prime%i ==0:
            factors_of_prime.append(i)
        
        else:
            None
            
    
    for i in factors_of_prime:
        
        
        if is_prime(i):
            print i
            
            
def is_prime(num):
    
    if num > 1:
        
        for i in range(2, num):
            
            if (num % i) == 0:
                return False
                break
        
        else:
            return True
                

#### End OF MARKER


### YOUR CODE FOR get_nth_prime() FUNCTION GOES HERE ###
def get_nth_prime(term):

    if type(term)== float:
        return None

    nth_term = 0

    for i in range(1,100000):
        if is_prime(i):
            nth_term = nth_term + 1

        if nth_term == term:
            return i
            break

if __name__ == '__main__':
    output_prime_factors(23)
    print get_nth_prime(4)
