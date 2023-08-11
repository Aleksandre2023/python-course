my_string = "hello, student!"
print(type(my_string))

my_string = 'hello, student!'
print(type(my_string))

print(my_string[0])
print(my_string[1: 5])

for c in my_string:
    print(c)

print("The Lenght of the string is", len(my_string))


# comparison of the strings
print("A" < "a", ord("a"), ord("a"))
print("cookie" < "Cookie")
print("00:15"<"12.45")
print("9888888554545346634567347357" < "a")

# concatination
str1 = "chocolate"
str2 = "muffin"
str3= str1 + " "+ str2
print(str3)

str4 = (str1 + " ")*100 + str2
print(str4)

#convert
str5 = str(10.23)

# Empty string
empty_string = '' # or '' 

#long string
print('''
0_o 
''')

# \n 