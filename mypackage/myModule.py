def tp_n (items, n):
    """ Return the top n items in an arry, in desc order

    Args:
        items (array) : list or array-like object
        n (int) : num of items to return

    Return:
        array: top n items, in desc order

    Egs: 
        >>> top_n([8,3,2,7,4]),3) == [8,7,3]

    """

    sorted_items = sorted(items, key=lambda x:x, reversed=False)
    return sorted[-n:]
