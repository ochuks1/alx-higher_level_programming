def max_integer(list=[]):
    """
    Find the maximum integer in a list.

    Prototype: def max_integer(list=[]):
    Returns the maximum integer in the list, or None if the list is empty.
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
