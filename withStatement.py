with open('example3.txt','a+') as file:
    file.seek(0)
    content = file.read()
    print('\noutput of example3.txt before append',content)
    file.write('\nMarkurdi')
with open('example3.txt','r') as file2:
    contentappend = file2.read()
    print('\noutput of example3.txt After append',contentappend)
