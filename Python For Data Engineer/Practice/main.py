print("Hello World")

print("Hello Samiran")

print("Hello Samiran Samanta", 1)

print("Hello Samiran Samanta", 1, "Delta")

# Multiple assignments
x, y, z = 10, 5, 6

'''This is a multiline comment
in python'''

# Multiline code

total_sum = 10+20\
            +30+20+20+20

# or

total_sum = (10+20
             +30+20+20+20)

print(total_sum)

x = 1
if x == 1:
    print("Wow")


# Typecasting

a = 10
b = "10"

print(type(b))

new_b = int(b)
print(type(new_b))

x = "Samiran"
print(x[1])

print(x[0:3])

x = "Samiran Samanta"
print(x.lower())
print(x.capitalize())
print(x.upper())
print(x.replace('S', 'Z'))

x = "Samiran Samanta Data Engineer"

x_list = x.split(' ')
print(x_list)

x = "raw_data.csv"

if x.endswith(".csv"):
    print("csv file")
if x.startswith("raw"):
    print("raw data...")


statement = "Hello Samiran, What are you doing. Hey Samiran I'm talking to you."

print(statement.count("Samiran"))


demo_string = "Hello"

demo_var = "10"

print(demo_string.isnumeric())

print(demo_var.isnumeric())

demo_var = "10abc"
print(demo_var.isalnum())

x = 1000

if (x == 10):
    print("X is 10.")
elif (x > 100):
    if((x > 100) and (x < 200)):
        print("X is between 100 and 200.")
    else:
        print("Greater than 200.")
else:
    print("X is not 10.")


# ...............Loops.................

my_list = ["orders", "products", "customers"]

for i in my_list:
    print(i)

for i in range(1, 11):
    print(i)

for i in my_list:
    if(i.lower() == "orders"):
        print("Table order...")
    else:
        print("No Table order...")

for i in my_list:
    print(i)
    for x in i:
        print(x)