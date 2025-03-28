def even_check(number = 2):
    if isinstance(number, (int,float)):
        return (number % 2 == 0)
    else:
        return 'Not a number'
    
print(even_check())


# RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST
print('------------------------------------')
def even_list_check(list = [1,2,3,4]):
    for number in list:
        if even_check(number) == True:
            return True
        else:
            pass
        
    return False # If it doesn't return True after checking all numbers in the list, return False
        
print(even_list_check())


# RETURN EVEN NUMBERS
print('------------------------------------')
def even_numbers_list_extractor(list = [1,2,3,4]):
    even_numbers = []
    for number in list:
        if even_check(number) == True:
            even_numbers.append(number)
        else:
            pass

    return even_numbers
        
print(even_numbers_list_extractor())