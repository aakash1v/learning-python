'''Note: All string methods returns new values. They do not change the original string.'''

# isprintable()	Returns True if all characters in the string are printable
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

# isspace()	Returns True if all characters in the string are whitespaces

# istitle()	Returns True if the string follows the rules of a title
str = "This Is Title"
print(str.istitle())

# isupper()	Returns True if all characters in the string are upper case

# join()	Converts the elements of an iterable into a string
mytuple =('AAaksh','Demon','No one nows')
x = "# ".join(mytuple) #joins between the string..ha haha
print(x)


myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)    #join between the keys...

print(x)
# ljust()	Returns a left justified version of the string
txt = "banana"      #add widespace to right or move the string to right what do you wanna say...

x = txt.ljust(20)

print(x, "is my favorite fruit.")
# lower()	Converts a string into lower case - iknow
# lstrip()	Returns a left trim version of the string -iknow
str= "    aakash"
print(str.lstrip())

# maketrans()	Returns a translation table to be used in translations
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))
# partition()	Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)
# replace()	Returns a string where a specified value is replaced with a specified value
txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)

# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts

# rsplit()	Splits the string at the specified separator, and returns a list
txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)

# rstrip()	Returns a right trim version of the stringtxt = "apple, banana, cherry"

# split()	Splits the string at the specified separator, and returns a list
txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)
# splitlines()	Splits the string at line breaks and returns a list
txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
txt = "Welcome to my 2nd world"
x = txt.title()
print(x)
# translate()	Returns a translated string
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

# upper()	Converts a string into upper case
str = 'lower'
print(str.upper())
# zfill()	Fills the string with a specified number of 0 values at the beginning
a = "hello"
b = "welcome to the jungle"
c = "10.000"
# fill zeroes at starting...
print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))