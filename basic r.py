#================read the file=============

f=open('test.txt','r')
print(f.read(10))
#=================read only parts of the file===========

f=open('test.txt','r')
print(f.read(5))

#==================readlines of the file================

f=open('test.txt','r')
print(f.readline())

#=================close the file===================

f=open('test.txt','r')
print(f.readline())
f.close()

#=================python file write(append,overwrite(write))===============
#f=open('test.txt','and overwrite the content:')
f=open('test.txt1','w')
f.write('woops!i have deleted the content')
f.close()

#=================file in append==============================
# f=open('test.txt1','a')
# f.append('that content is deleted')
# f.close()

#==============w3school===============

#f = open("D:\\myfiles\welcome.txt", "r")
# a=’ ‘
# for i in range(len(str)):
#     a+=1
#     print(a)

#print(f.read()) #it gives error   
my='laxmi'
blog='rajasri'      
print(my+blog * 2)

print(my *3 + blog +'7'+'')




