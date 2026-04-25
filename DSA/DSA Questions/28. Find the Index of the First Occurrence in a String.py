def strStr(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

haystack = str(input("Enter the string: "))

needle = str(input("Enter the needle: "))
print(strStr(haystack=haystack, needle=needle))
