arn = "arn:aws:iam::123456789012:user/johndoe" # AWS ARN String

print(arn.split("/")[1]) # Extract the username from arn string

username = arn.split("/")[1]
print(username.upper()) # Print the username in uppercase
print(arn.split("/")[1].upper()) # This also works to print the username in uppercase in one line

str1 = "Hello"
str2 = "World!"
print(str1+" "+str2) # Concat two strings

import re
str = "A quick brown fox."
pattern = r"quick"
match = re.match(pattern, str)

if match:
    print("Match found: ", match.group())
else:
    print("No match found.")