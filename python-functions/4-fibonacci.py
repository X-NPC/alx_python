fibonacci_list = []

def fibonacci_sequence(n):
    if n > 1:
        for n in (1,):
            sequence = (n-1) + (n-2)
            fibonacci_list.append (sequence)
    else:
        fibonacci_list = []
    return fibonacci_list

    
