def is_password_valid(pword):
    is_digit = 0
    is_valid = True
    if 6 <= len(pword) <= 10:
        pass
    else:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    if pword.isalnum():
        pass
    else:
        is_valid = False
        print("Password must consist only of letters and digits")
    for el in pword:
        if el.isdigit():
            is_digit +=1
    if is_digit < 2:
        is_valid = False
        print("Password must have at least 2 digits")
    if is_valid:
        print("Password is valid")
    return is_valid


password = input()
result = is_password_valid(password)