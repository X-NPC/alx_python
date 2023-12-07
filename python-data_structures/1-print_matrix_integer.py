# Okay, I don't really know what to do.#

#matrix is like creating a list in a list. so 

def print_matrix_integer (matrix=[[]]):
    #why don't I try to creat a while loop that adds 3 consecutive numbers in list until it reaches 9 
    # and adds the lists in another list
    # And then creat a row for each number
    i = 1
    while i == 1:
        matrix_list = [[i, i+1, i+2], [i+3, i+4, i+5], [i+6, i+7, i+8]]
        i = 0
        print( "{}\n{}\n{}" .format(matrix_list[i], matrix_list[i+1], matrix_list[i+2]))
        
        
print(print_matrix_integer())
                    
        