class YourClass(object):
    classy = 'class value!'

dd = YourClass()

print(dd.classy)

dd.classy ='inst value!'
print(dd.classy)

del dd.classy

print(dd.classy)

