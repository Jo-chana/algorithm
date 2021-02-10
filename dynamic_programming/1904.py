import sys
N = int(sys.stdin.readline())

if N <= 2:
	print(N)
	exit()

d = [1, 2, 0]

for i in range(2, N):
	d[i % 3] = (d[(i+1) % 3] + d[(i+2) % 3]) % 15746
	if i == N-1:
		print(d[i % 3])
