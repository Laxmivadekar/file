f=open('xyz.txt')
content=f.read()
print(content)
f.close()
print('_____________________________________________________________________')
#=================================================================================
# f=open('xyz.txt','r')
# f.read()
# f.close()
print('____________________________no. of charactes we want yo read_________________________________________')
f=open('xyz.txt')
content=f.read(100)
print(content)
f.close()
print('_____________________________________________________________________')
#===============================================================================
f=open('xyz.txt')
content=f.read(11)
print('1:',content)
content=f.read(1)
print('2:',content)
f.close()
print('____________________________rt-Read in text format________________________________________')
#=============================================================================
f=open('xyz.txt','rt')
content=f.read()
for line in content:
    print(line)
print('______________________________rt-as it is before but one extra line after every line_______________________________________')
#===============================================================================
f=open('xyz.txt','rt')
for line in f:
    print(line)
print('_________________________________rt -side by side____________________________________')
#================================================================================
f=open('xyz.txt','rt')
for line in f:
    print(line,end='')
f.close()
print('_____________________________________________________________________')
#================================================================================
f=open('xyz.txt')
content=f.read(11)
print('1:',content)
content=f.read(1)
print('2:',content)
f.close()
print('_________________________Readline____________________________________________')
#================================================================================
f=open('xyz.txt','rt')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
# f.close()
print('________________________________readlines_________________________________________________')
#=========================================================================================
f=open('xyz.txt','rt')
print(f.readlines())
print("______________________________________________________________________________")

#===========================================================================================
f=open('abc.txt','a')
a=f.write('\n**you are lucky**')
print(a)
f.close()
