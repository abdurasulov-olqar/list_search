def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    m = max(data)
    for i in data:
        if m > i and i % 2 == 1:
            m = i
    if m % 2 ==1:
        return m
    else:
        return -1
