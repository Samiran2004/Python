def defangIPaddr(address) -> str:
    stringList = address.split(".")
    newAddress = "[.]".join(stringList)
    return newAddress

address = str(input("Enter the ip: "))
print(address)
print(defangIPaddr(address))
