# Palindrome Permutation: Given a string, write a function to check if it is a permutation of
# a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
# permutation is a rearrangement of letters. The palindrome does not need to be limited to just
# dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat'; "atc o eta·; etc.)



def checkPalindrome(input):
    flags = [0] * 128

    for char in input:
        if (char != ' '):
            flags[ord(char.lower())] += 1

    num_of_odd = 0
    for flag in flags:
        if (flag % 2 == 1):
            num_of_odd += 1
        
        if (num_of_odd > 1):
            return False

    return True


def checkIfPalindromeAnswer(input):
    flag = 0

    for char in input:
        ordinal = ord(char.lower()) - ord('a')
        if (ordinal >= 0):
            flag ^= (1 << ordinal)
    
    mask = flag - 1
    odd_count = flag & mask
    return odd_count <= 1   



input = "Tact  Coa"
print("is palindrome: " + str(checkIfPalindromeAnswer(input)))