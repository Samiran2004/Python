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
search = re.search(pattern, str)

if search:
    print("Search found: ", search.group())
else:
    print("Search Element Not Found.")

if match:
    print("Match found: ", match.group())
else:
    print("No match found.")

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"
replace_str = "red"
new_txt = re.sub(pattern, replace_str, text)
print("Modified text: ", new_txt)

text = "apple,banana,orange,grape"
pattern = r","
split_result = re.split(pattern, text)
print("Split result: ",split_result)

print(len(username)) # Print the length of the username
# print(len(arn.split("/")[0]))

mod_arn = arn.replace(username, "samiran") # Modify the username
print(mod_arn)

text = "   Some spaces around   "
stripped_txt = text.strip() # String strip
print("Stripped text: ", stripped_txt)

text = "Python is awesome"
substring = "is"
if substring in text:  # Found substring
    print(substring, "found in the text")