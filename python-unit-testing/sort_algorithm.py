

def sort_algorithm(lst):
    """Returns a sorted list given a list input

    Parameters
    ----------
        lst : list
            List of integers to be sorted
    Returns
    -------
        list
            Sorted list of integers
    """

    if not all([isinstance(x, int) for x in lst]):
        raise TypeError('Input should be list of integer values')

    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst
