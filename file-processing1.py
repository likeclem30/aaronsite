file = open('example.txt','r')
content = file.read()
contentline = file.readlines()
print('output of file.read()',content)
print('output of file.readlines()',contentline,'\n')

print('Date type of a file variable :',type(file))
print('Date type of a content variable type :',type(content))