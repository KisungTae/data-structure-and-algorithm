# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: if implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"

def replace(url, size):
    num_of_space = 0

    for i in range(size):
        if (url[i] == ' '):
            num_of_space += 1
    
    push_index = size - 1 + num_of_space * 2

    for i in reversed(range(size)):
        if (url[i] == ' '):
            url[push_index] = '0'
            url[push_index - 1] = '2'
            url[push_index - 2] = '%'
            push_index -= 3
        else:
            url[push_index] = url[i]
            push_index -= 1


url = ['M', 'r', ' ', 'J', 'o', 'h', 'n', ' ', 'S', 'm', 'i', 't', 'h', ' ',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '',  '']

print("url: " + str(url))
print("replacing.....")
replace(url, 13)
print("url: " + str(url))
