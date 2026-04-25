from typing import List

def numUniqueEmails(emails: List[str])-> int:
    unique = set()

    for e in emails:
        local, domain = e.split("@")
        local = local.split("+")[0]
        local = local.replace(".", "")
        unique.add((local, domain))
    
    return len(unique)

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
result = numUniqueEmails(emails=emails)
print(result)