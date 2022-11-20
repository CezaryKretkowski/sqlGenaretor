import sys


filePAth = sys.argv[1]
fileName = sys.argv[2]
f=open(filePAth,'r')
newFiell=open(fileName+".sql",'w')
iterator=1;
names=f.read().splitlines()

newFiell.writelines("DELETE FROM "+fileName+";\n\n")
for i in names:
    line = "insert into "+fileName+" values("+str(iterator)+","+i+");"
    newFiell.writelines(line+"\n")
    iterator+=1
       
