"""a function that divides two integers"""

def safe_print_division(a=0, b=1):
    # custom exception errors when things go wrong (valueError, typeError, denominator=0)
    try:
        the_result = a/b
    except ValueError:
        print ("Please use a valid number")
    except TypeError:
        print ("Please input a valid datatype.")
    except ZeroDivisionError:
        None
    finally:
        print("Inside result: {}" .format(the_result))
    



    return the_result

# I didn't know I could put exception in a function till now

# speciall variable from Mesoud

if __name__ == "__main__":
    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))