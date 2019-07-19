def square(x):
    print (x * x)
    return x * x

# square(4)

def sum_of_squares(x,y):
    ans = ((x * x) + (y * y))
    print (ans)
    return ans

sum_of_squares(1,1)


# sum_of_squares('a', 3) //Can't multiply string with an int



def sqrt(num, guess=1): 
    print ("Finding square root of", num, "starting with guess:", guess)

sqrt(36)

# //-------------------/----------------------------------
#compound statements

def percent_difference(x,y):
    diff = abs(x - y)
    return 100 * diff / x

result = percent_difference(40,100)
print (result, "<---The result is")

#Conditionals

def absolute(x):
    if x > 0:
        print (x)
        return x
    elif x == 0:
        print (0)
        return 0

    else:
        print (-x)
        return -x

absolute(3)

a = 6
b = 3
if a > 5:
    if b > 6:
        print("a is more than 5 and b is more than 6")
    else:
        print("a is more than 5 BUT b is not more than 6")
else:
    print("a is not more than 5")


#compound statements-----------------------------------------------------------

def sqrt(x, guess = 0.0): 
    if x < 0: 
        return None 
    
    if good_enough(guess, x): 
        return guess 
    
    else: 
        new_guess = improve_guess(guess, x)  # let's just call it `guess`
        return sqrt(x, new_guess)

def good_enough(guess, x): 
    if abs(guess * guess - x) < 0.1: 
        return True
    else: 
        return False 

def improve_guess(guess, x): 
    if guess < x: 
        return guess + 0.1 
    else: 
        return guess - 0.1 

print sqrt(4, 1.8)

#-----------------------------------------------------------------------------------------

