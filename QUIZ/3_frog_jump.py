from sys import argv

start,finish,step = map(int, argv[1:4])
count = 0

for i in range(start, finish, step): count+=1
print count
