# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.


def checkIfPermutation(prev_string, next_string):
    if (len(prev_string) != len(next_string)):
        return False
    
    if (addup(prev_string) == addup(next_string)):
        return True

    return False

def addup(string): 
    sum = 0
    for char in string:
        sum += ord(char)

    return sum


def checkIfPermutationAnswer(prev_string, next_string):
    if (len(prev_string) != len(next_string)):
        return False
    
    flags = [0] * 128

    for char in prev_string:
        flags[ord(char)] += 1

    for char in next_string:
        flags[ord(char)] -= 1
        if (flags[ord(char)] < 0):
            return False

    return True


prev_string = "abc"
next_string = "cba"

# print("is permutation: " + str(checkIfPermutation(prev_string, next_string)))
print("is permutation: " + str(checkIfPermutationAnswer(prev_string, next_string)))

