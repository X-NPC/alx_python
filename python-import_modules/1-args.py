"""This program should be able to list number of arguments"""
# first I need to know what an argument is
# then I 
# use a if statement to determined what to do with 1 argument and otherwise
# elif --> args==0 print (0 arguments.)
# else:-->  for loop to iterate in the multiple arguments

# why don't I create a dictionary

from sys import argv
# I didn't know that I needed to import sys lol

def print_arguments ():
    num_of_args = len(argv) - 1
    
    print(f"{num_of_args} arguemnt{'s' if num_of_args != 1 else ''}:", end='')
    
    if num_of_args == 0:
        print('.')
    else:
        print()
        
        for i, arg in enumerate(argv[1:], start=1):
            print(f"{i}: {arg}") 
             
if __name__ == "__main__":
    print_arguments()
    
    
print_arguments()
