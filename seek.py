f=open('abc.txt')
print(f.readline(),end='')
f.seek(1)
print(f.readline(),end='')
f.seek(60)
print(f.readline(),end='')
f.seek(65)
print(f.readline())
f.close()

