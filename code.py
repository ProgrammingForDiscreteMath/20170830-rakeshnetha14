# 1
# Replace if-else with try-except in the the example below:

def fourth_element_of_list(L,i):
    """
    Return the nth element of ``L`` if it exists, ``None`` otherwise.
    """
    try:
        return L[i]
    except IndexError:
        return None
    

# 2
# Modify to use try-except to return the sum of all numbers in L,
# ignoring other data-types

def sum_of_numbers(L):
    """
    Return the sum of all the numbers in L.
    """
    s = 0
    for l in L:
        try:
            if type(l) is int or type(l) is float:
                s += l
        except TypeError:
            s
    return s

# TEST
# sum_of_numbers([3, 1.9, 's']) == 4.9
sum_of_numbers([3, 1.9, 's'])
