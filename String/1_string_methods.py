'''Note: All string methods returns new values. They do not change the original string.'''

# capitalize()	Converts the first character to upper case
str = 'this is my string'
print(str)
new_str = str.capitalize()
print(new_str)
print('aakahs kumar'.capitalize())  #only first word is captilize...:(

# casefold()	Converts string into lower case
str = 'AAkash Kumar'
print(str.casefold())

# center()	Returns a centered string
x = str.center(20)
print(x)

# count()	Returns the number of times a specified value occurs in a string
mystr = 'This is my string. and my string is the best string in the whole string world.'
print("Number of times 'string' in this string :",mystr.count('string'))

# encode()	Returns an encoded version of the string
print(str.encode())

# endswith()	Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
print(txt.endswith("my world."))

# expandtabs()	Sets the tab size of the string
txt= '\thello'
print(txt.expandtabs(50))

# find()	Searches the string for a specified value and returns the position of where it was found
print(str.find('string'))   #returns -1 if the value not find...

# format()	Formats specified values in a string
a = 5
print("THis is my string..and my special value {}".format(a))

# format_map()	Formats specified values in a string        -

# index()	Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
#search only btw 5 to 10
x = txt.index("e", 5, 10)
print(x)

# isalnum()	Returns True if all characters in the string are alphanumeric
a = '5'
print(a.isalnum())
# isalpha()	Returns True if all characters in the string are in the alphabet


# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
c  = "1234"
print(a.isdecimal())
print(b.isdecimal())
print(c.isdecimal())
# isdigit()	Returns True if all characters in the string are digits

# isidentifier()	Returns True if the string is an identifier
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print("Check identifier making rules and conditions...")
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

# islower()	Returns True if all characters in the string are lower case

# isnumeric()	Returns True if all characters in the string are numeric


