i = 0
number_list = ""

while i != 100:
    number = str(i)
    #the line below addes a zero in front of numbers less that ten 
    number = number.zfill(2)
    space_between = ", "
    number_list = number_list + number + space_between
    i = i + 1
   
   #the below if statement clears the last unnessary commma (after 99)
    if i == 99:
        number = str(i)
        space_between = ""
        number_list = number_list  + number + space_between
        i += 1
    else:
        None


print ( "{}".format(number_list))
