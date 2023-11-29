def validate_password( password):
    string_password = str(password)
    condition_one = len(string_password)>= 8
    condition_two = string_password.isupper() 
    condition_three = string_password.islower()
    condition_four = string_password.isdigit ()
    if condition_one condition_two and condition_three and condition_four:
        return True
    else:
        return False

  

print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))
