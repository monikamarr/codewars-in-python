def area_or_perimeter(l , w):
    """return area or perimeter of a 4-sided polygon"""
    return l*w if l == w else 2 * (l + w)