def no_c (my_string):
    # list each characters
    letter = [x for x in my_string]
    
 # check if c and C are memeber of My_string and remove them
    if "c" in letter:
        letter.remove ("c")
        
    #convert the list into tuple because list has no join() attribute and return
        my_string = tuple(letter)
        edited = "".join(my_string)
        return edited
    elif "C" in letter:
        letter.remove("C")
        my_string = tuple(letter)
        edited = "".join(my_string)
        return edited
# if c and C are not members just return the string as it is
    else:
        return my_string
        
