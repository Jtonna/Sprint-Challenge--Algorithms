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

    #  Slices the first 2 letters off of the passed in parameter (word)
    the_word = word[2:]

    #  If the length of the passed in parameter(word) is less than or equal to 1, we just return count since there is no way it can contain "t" & "h".
    if len(word) <= 1:
        return count

    #  If the "word" array index position 0 is a "t" AND position 1 is an "h" we can do something
    if word[0] == "t" and word[1] == "h":
        #  The something we are going to do is increment count + 1 since "th" was found
        count += 1
        #  Then we will return the rest of the_word (excluding the two indexes we proccessed) to the function as well as the new value of count
        return count_th(the_word, count)
    #  If word[0] is not t, we need to do something
    elif word[0] != "t":
        """What were going to do is set the_word to the whole current (mutated) array minus the
        first letter as well as the current count so it doesnt get reset by the default value we spefified
        """
        the_word = word[1:]
        return count_th(the_word, count)
    #  If word[0] & word[1] are both t we need to do something
    elif word[0] == "t" and word[1] == "t":
        # We are going to use a slice stop|start|stop and remove word[0] which is one of the t's and return the word and the count + 1
        count += 1
        the_word = word[1:0:2]
        return count_th(the_word, count)
    # Once theres nothing left to do we are just going to return the_word and the current count
    else:
        return count_th(the_word, count)

#print(count_th("thThTHtheresof"))
