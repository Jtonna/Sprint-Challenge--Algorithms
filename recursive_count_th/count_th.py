'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count = 0):
    """ Plan
    If the length of the param(word) is less than or equal to 1, we just return count

    if
        return (calls count)
    elif
        return (calls count)
    else
        return (calls count)
    """

    """If the length of the passed in parameter(word) is less than or equal to 1, we just return count. """
    if len(word) <= 1:
        return count
    
    the_word = word[2:]
    # Slices the last 2 letters off of the passed in parameter (word)

    pass
    
