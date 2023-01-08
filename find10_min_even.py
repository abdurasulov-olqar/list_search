def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    m = max(data)
    for i in data:
        if m > i and i%2 == 0:
            m = i
    if m%2 ==0:
        return m
    else:
        return -1


