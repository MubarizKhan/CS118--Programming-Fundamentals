## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade(obt_marks):
    num = int(round(marks))
    if obt_marks >= 90:
        return 'A+'

    if obt_marks >= 86:
        return 'A'

    if obt_marks >= 82:
        return 'A-'

    if obt_marks >= 78:
        return 'B+'

    if obt_marks >= 74:
        return 'B'

    if obt_marks >= 70:
        return 'B-'

    if obt_marks >= 66:
        return 'C+'

    if obt_marks >= 62:
        return 'C'

    if obt_marks >= 58:
        return 'C-'


    if obt_marks >= 54:
        return 'D+'

    if obt_marks >= 50:
        return 'D'

    if obt_marks >= 0:
        return 'F'

#### End OF MARKER


#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####
def grades_val(x):

    if x == 'A':
        return 4.00
 
    if x == 'A-':
        return 3.67

    if x == 'B+':
        return 3.33

    if x == 'B':
        return 3.00
 
    if x == 'B-':
        return 2.67

    if x == 'C+':
        return 2.33

    if x == 'C':
        return 2.00

    if x == 'C-':
        return 1.67

    if x == 'D+':
        return 1.33

    if x == 'D':
        return 1.00

    if x == 'F':
        return 0.00

def calculate_sgpa(sub1, sub2, sub3):

    total_marks = 0
    total_subs = 0.00

    if sub1 != "nothing":
        total_subs = total_subs + 1
        total_marks = total_marks + grades_val(sub1)
    

    if sub2 != "nothing":
        total_subs = total_subs + 1
        total_marks = total_marks + grades_val(sub2)

    
    if sub3 != "nothing":
        total_subs = total_subs + 1
        total_marks = total_marks + grades_val(sub3)
    
    if total_subs == 0:
        return 0
    
    
    SGPA =  total_marks / total_subs
    
    return SGPA


    
    
    
    
#### End OF MARKER




if __name__ == '__main__':
    print get_grade(50)
    print calculate_sgpa('A', 'B', 'nothing')
