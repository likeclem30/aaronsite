loc =['kaduna','abuaja','lagos','kano']
file = open('example3.txt','a')
file.write('\nNames of loc\n')
for i in loc:
    file.write(i+'\n')
file.close()