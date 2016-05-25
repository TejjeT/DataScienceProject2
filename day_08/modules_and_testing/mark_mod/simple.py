def positive_divide(x,y):
    """
    compute the ratio between positve x and y values
    """
    if x < 0 or y < 0:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    return x / y

if __name__=="__main__":
    print positive_divide(8,2)
