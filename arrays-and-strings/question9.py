# 1.9 String Rotation: Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 using only one
# call to isSubString (e.g., "waterbottle" is a rotation of" erbottlewat").



def check_if_rotation(s1, s2):
    joined_s2 = "".join([s2, s2])
    return joined_s2.find(s1) > 0



s1 = "waterbottle"
s2 = "erbottlewat"

print(str(check_if_rotation(s1, s2)))
