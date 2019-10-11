'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count = 0):
    """ Plan
    If the length of the param(word) is less than or equal to 1, we just return count
    Were going to have to slice up the string from its original array (since strings are technically arrays)
    We can use and if, elif & else statement that calls back on count_th and passes it data to update the count (how many "th"'s we found in the string)
    """

    #  If the length of the passed in parameter(word) is less than or equal to 1, we just return count since there is no way it can contain "t" & "h".
    if len(word) <= 1:
        return count
    
    #  Slices the last 2 letters off of the passed in parameter (word)
    the_word = word[2:]

    #  If the "word" array index position 0 is a "t" AND position 1 is an "h" we can do something
    if word[0] == "t" and word[1] == "h":
        #  The something we are going to do is increment count + 1 since "th" was found
        count + 1

    pass
    
