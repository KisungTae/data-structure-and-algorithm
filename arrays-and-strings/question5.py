# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae -> false




def checkIfOneEditAway(prev_str, next_str):

    diff = len(prev_str) - len(next_str)
    if (abs(diff) > 1): 
        return False
    
    bigger = prev_str if diff >= 0 else next_str
    smaller = prev_str if diff < 0 else next_str 

    bigger_index = 0
    smaller_index = 0

    count_edit = 0
    while bigger_index < len(bigger) and smaller_index < len(smaller):
        if (bigger[bigger_index] == smaller[smaller_index]):
            bigger_index += 1
            smaller_index += 1
        else:
            count_edit += 1
            if (count_edit > 1): 
                return False
            bigger_index += 1
            if (abs(diff) == 0):
                smaller_index += 1
    
    return True




prev_str = "pale"
next_str = "pale"


print("is one edit away: " + str(checkIfOneEditAway(prev_str, next_str)))

