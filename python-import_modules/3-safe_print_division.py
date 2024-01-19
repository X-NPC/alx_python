"""a function that divides two integers"""

def safe_print_division(a=0, b=1):
    the_result = a/b
    return the_result


a = 12
b = 2
result = safe_print_division(a, b)
# custom exception errors when things go wrong (valueError, typeError, denominator=0)

try:
    safe_print_division
    
except ValueError:
    print ("Please use a valid number")
except TypeError:
    print ("Please input a valid datatype.")
except ZeroDivisionError:
    None
    
finally:
    print("Inside result: {}" .format(result))
    

print("{:d} / {:d} = {}".format(a, b, result))