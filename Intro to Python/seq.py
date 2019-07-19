for ingredient in "sugar","milk","tea-leaves":
    print ("put in", ingredient)


for i in range(1,6):
    print ("*" * i)

for i in range(6,0,-1):
    print ("*" * i)

n = 0.20
while n < 1:
    print (n) 
    n += 0.10

print ("done")

#--------------------------------------------
def fib(n): 
    if n <= 1:
        return n 
    
    else: 
        return fib(n-1) + fib(n-2)
#-------------------------------------------------

#lists
# 
multi = [1,2,3,"fg", 4, 5, 7]
print(multi)
print(len(multi))


print("fg" in multi) #memebership check



def make_tea(ing):
    for i in ing: 
        print ("Put", i, "..")
        
        
ingredients = ['water', 'cinnamon', 'tea leaves', 'sugar', 'milk']
make_tea(ingredients)

list = [1,33,55,4,67,54,2,44,67,32,44]
def count(s,value):
    counter = 0
    for i in s:
        if value in s:
            counter += 1
        
    return counter

print(count(list, 1))

#modifying elements
list[0] = 55
print(list)


print(list[3:])
print(list[:3])
print(list[4:7])
    
#_______________________________--Nested Sequences---------------------------

pairs = [
    [1,2,3,4,5], [6,7,8,9,10,11], [12,13,14,15,16,17]
    ]

print(pairs[0][1],"<----")
for x in pairs:     # but we know that a is a "pair" 
    print ('x=', x )


a = [1.1, 2.3, 3.3, 4.4,5.5, 6.6]
a.append(987)

print(a)
a.insert(2,1) #a.(index,object)
a.insert(0, "I got u")
print(a)

a.extend(["work", "hard", "play","hard"])
print(a)

# for i in a:
#     a.remove(i)
# print(a,"<----")

a.pop(0)
print(a)

print(a.index(3.3))

a.reverse()
print(a)


# ----------- Strings ---------------------------------------------

s = "This_is_a_dummy_string"
print(s[3:])
print(s[0])
print(len(s))
print(s[0:5])



nums = [1,2,3,4,5,6,7,8,9,10]
empty = []

for i in nums:
    if i % 2 == 0:
        empty += [i]

print(empty,"<----")

#--------------Tuples---------------
# Tuples are just like lists but are immutable; which means nothing can be deleted ot added in
# the tuple

digits = (1,8,2,8,23,24,24)
print(digits[3:], "<---ale")
