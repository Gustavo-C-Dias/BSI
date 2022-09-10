# V[X+1] = 3
# V[X+2] = 10
# V[X+3] = 9
# V[X*4] = 33
# V[X*1] = 8
# V[X*2] = 10
# V[X*3] = 1
# V[ V [X+Y]] = 6
# V[X+Y] = 1
# V[8-V[2]] = 2
# V[V[4]]= X
# V[ V[ V[7]]]= X
# V[V[1]*V[4]]= X
# V[X+4] = 1

V = [2,6,8,3,10,9,1,21,33,14]
x = 2
y = 4

print(V[x+1])
print(V[x+2])
print(V[x+3])
print(V[x*4])
print(V[x*1])
print(V[x*2])
print(V[x*3])
print(V[V[x+y]])
print(V[x+y])
print(V[8-V[2]])
print(V[x+4])
# print(V[V[4]])
# print(V[V[V[7]]])
# print(V[V[1]*V[4]])







 