l = ['James','Cynthia','Moses','Jack']
file = open('example3.txt','w')
for a in l:
    file.write(a+'\n')
file.close()

