def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    maxi = 0
    mini = data[0]
    for i in data:
        if maxi < i:
            maxi = i
        if mini > i:
            mini = i
    return mini + maxi
