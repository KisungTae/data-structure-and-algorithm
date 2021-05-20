# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).




def compress(input):

    current_char = ""
    count = 0
    compressed = []

    for i in range(len(input)):
        if (current_char == input[i]):
            count += 1
        else:
            compressed.append(current_char)
            if count > 0:
                compressed.append(str(count))
            count = 1
            current_char = input[i]

    compressed.append(current_char)
    compressed.append(str(count))
    compressed_input = "".join(compressed)

    if (len(compressed_input) > len(input)):
        return input
    return compressed_input




def compressAnswer(input):
    count_consecutive = 0
    compressed = []
    for i in range(len(input)):
        count_consecutive += 1
        if i + 1 >= len(input) or input[i] != input[i + 1]:
            compressed.append(input[i])
            compressed.append(str(count_consecutive))
            count_consecutive = 0
    
    return "".join(compressed)


input = "aaaaaaaaaa"
print("compressed: " + compressAnswer(input))