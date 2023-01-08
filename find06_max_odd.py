def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    m = data[0]
    for i in data:
        if m<i and i % 2 == 1:
            m = i
    return m