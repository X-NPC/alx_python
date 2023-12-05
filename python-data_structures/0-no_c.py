# this function removes c or C or both from a string when it's called

# I am using two ways: the first if it contains both small and capital C, the second if it contains either

def no_c (my_string):
    
    # list each characters for the two conditions
    letter = [x for x in my_string]
    
# use this method if it contains both c and C
    if "c" in letter and "C" in letter:
        characters_to_remove = ["c", "C"]
        filtered_characters = [filter(lambda: y not in characters_to_remove, my_string)]
        
        edited = "".join(filtered_characters)
        return edited

    
 # check if c and C are memeber of My_string in two if statements and remove them
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
        
print(no_c("Chicago"))