import sys
n=int(sys.argv[1])
m=2*n+1
print('\n'.join([''.join([i for i in r]) for r in [[('*',' ')[n-abs(n-x)<abs(n-y)] for x in range(m)] for y in range(m)]]))