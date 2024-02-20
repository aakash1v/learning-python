file= open('youtube.txt','w')

try:
    file.write('chai aur code')
except Exception as e:
    print(e)
finally:
    file.close()

# second way...
with open('youtube.txt','r') as f:
    text = f.read()
    print(text)
    

