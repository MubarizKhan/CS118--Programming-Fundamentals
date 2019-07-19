# import os.path

from pathlib import Path

data_folder = Path("C:/Users/Owner/Desktop/Python/res") 

file_to_open = data_folder / "dummy.txt"

f = open(file_to_open)

# print(f.read())

    # “ r “, for reading.
    # “ w “, for writing.
    # “ a “, for appending.
    # “ r+ “, for both reading and writing
l = []
for line in f:
    l.append(line)
    print(l)

file = open('geek.txt','w') 
file.write("This is the write command") 
file.write("youvr got a roomate") 
file.close() 



f.close()