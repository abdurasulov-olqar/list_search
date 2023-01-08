def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    m = 2
    for i in data:
        if m<=i and i % 2 == 0:
            m = i
    return m

print(find_max_even([1, 4, 3, 8, 5]))
