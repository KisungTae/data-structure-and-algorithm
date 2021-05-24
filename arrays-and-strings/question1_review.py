# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?


def checkIfCharUnique(str):
    for i in range(len(str) - 1):    
        prev_char = str[i]
        next_char = str[i + 1]
        if (prev_char == next_char):
            print(prev_char + " == " + next_char)
            return False
    return True


# string = "abcdeff"
# is_unique = checkIfCharUnique("".join(sorted(string)))
# print("is unique: " + str(is_unique))

 
# ANSWER
# 1. assume it is ASCII set


def checkIfCharUniqueAnswer(string):
    max_unique_char = 128
    if (len(string) > max_unique_char): 
        return False

    flags = [False] * max_unique_char
    for char in string:
        ascii_code = ord(char)
        if (flags[ascii_code]):
            print("duplicate char: " + char)
            return True
        else:
            flags[ascii_code] = True
    
    return True

# ANSWER
# 1. using bit

def checkIfCharUniqueWihtBit(string):
    flag = 0
    for char in string:
        index = ord(char) - ord('a')
        ascii_code = 1 << index
        if ((flag & ascii_code) > 0):
            print("duplicate char: " + char) 
            return True
        else:
            flag |= ascii_code

    return True


string = "aaabbb"
is_unique = checkIfCharUniqueWihtBit(string)
print("is unique: " + str(is_unique))
