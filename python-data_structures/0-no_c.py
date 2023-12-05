# this function removes c or C or both from a string when it's called

# I am using two ways: the first if it contains both small and capital C, the second if it contains either

def no_c (my_string):
    
    # list each characters for the conditions
    letter = [x for x in my_string]
    
    #condition one: contains both c and C
    
    if "c" in letter and "C" in letter:
        letter.remove ("c")
        letter.remove ("C")
   #convert the list into tuple because list has no join() attribute and return     
        my_string = tuple(letter)
        edited = "".join(my_string)
        return edited
    
    #condition two : contain only c
    
    elif "c" in letter:
        letter.remove ("c")
        
    
        my_string = tuple(letter)
        edited = "".join(my_string)
        return edited
    
    #condition 3: contains only C
    
    elif "C" in letter:
        letter.remove("C")
        my_string = tuple(letter)
        edited = "".join(my_string)
        return edited
    
    #conditon 4: doesn't contain c or C
    
    else:
        return my_string
        