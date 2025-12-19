from typing import List

def numUniqueEmails(emails: List[str])-> int:
    unique = set()

    for e in emails:
        local, domain = e.split("@")
        local = local.split("+")[0]
        local = local.replace(".", "")
        unique.add((local, domain))
    
    return len(unique)