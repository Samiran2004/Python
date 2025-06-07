arn = "arn:aws:iam::123456789012:user/johndoe" # AWS ARN String

print(arn.split("/")[1]) # Extract the username from arn string