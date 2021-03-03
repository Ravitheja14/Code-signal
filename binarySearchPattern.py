import re


def binarySearchPattern(s, pattern):
    count = 0
    new_s = ""
    new_pattern = ""
    for i in s:
        if i in 'aeiouy':
            new_s += "0"
        else:
            new_s += "1"
    for j in pattern:
        if j in 'aeiouy':
            new_pattern += "0"
        else:
            new_pattern += "1"

    x = len(re.findall(new_s, new_pattern))
    return x

# tested here with 3 scenario's


print(binarySearchPattern("ama", "amazingamazing"))
print(binarySearchPattern("code", "amazingamazing"))
print(binarySearchPattern("1111", "amazing"))