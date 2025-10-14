# def lengthOfLastWord(s: str)-> int:
#     if len(s) == 0:
#         return 0
#     strArr = s.split(" ")
#     return len(strArr[len(strArr) - 1])

def lengthOfLastWord(s: str)-> int:
    end = len(s) - 1
    while s[end] == " ":
        end -= 1
    start = end
    while start >= 0 and s[start] != " ":
        start -= 1
    return end - start

s = str(input("Enter the string: "))
print(lengthOfLastWord(s=s))
