
# You have to print the number of times that the substring occurs in the given string.
#  String traversal will take place from left to right, not from right to left.
def count_substring(string, sub_string):
    index = 1
    count = 0
    while index != -1:
        index = string.find(sub_string)
        if index >= 0:
            count += 1
        string = string[index+1:]
    print (count)



count_substring('ABCDCDC','CDC')