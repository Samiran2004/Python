arn = "arn:aws:iam::123456789012:user/johndoe" # AWS ARN String

print(arn.split("/")[1]) # Extract the username from arn string

username = arn.split("/")[1]
print(username.upper()) # Print the username in uppercase
print(arn.split("/")[1].upper()) # This also works to print the username in uppercase in one line