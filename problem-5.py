def is_negative_number(num):
    if num <= 0:
        return True
    else:
        return False


assert is_negative_number(3) == False
assert is_negative_number(-1) == True
assert is_negative_number(0) == False
print("success")
