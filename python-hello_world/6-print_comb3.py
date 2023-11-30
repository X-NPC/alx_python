number_list = []

for i in (0, 100):
    #number = number.zfull(2)
    if i % 10 > i % 100:
        number_list.append((str(i).zful(2))) 
       
    else:
        None    
    # space between = ", "
print ("{}" .format(number_list))
