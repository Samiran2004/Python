list_of_cloud = ["AWS", "Azure", "Google Cloud", "Digital Ocean", "Utho", "Alibaba", "Oracle"]
print(list_of_cloud)

#Add a new cloud Salseforce at the end
list_of_cloud.append("Salseforce")
list_of_cloud.append("IBM")
print(list_of_cloud)

#Add a new cloud index
list_of_cloud.insert(2, "Heroku")
print(list_of_cloud)

length = len(list_of_cloud)
print("Length of cloud is: ", length)

# Insert "Hello Cloud" to 0th index of list
list_of_cloud.insert(0, "Hello Cloud")
print(list_of_cloud)

# Iteration of a list
for cloud in list_of_cloud:
    print(cloud)

for i in range(1,11):
    print(i)