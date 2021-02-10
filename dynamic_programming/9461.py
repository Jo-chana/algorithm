from sys import stdin
c = []
for _ in range(int(stdin.readline())):
	c.append(int(stdin.readline()))

for N in c:
	d = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
	if N < 11:
		print(d[N-1])
	else:
		for i in range(10, N):
			d.append(d[i-5] + d[i-1])
		print(d[-1])


'''
	An = An-5 + An-1 수열 문제이다.
	문제에서 예제 케이스를 그대로 가져와 d 배열로 이용하였다.
	피보나치 수열과 비슷한 알고리즘이어서 특별한 어려움은 없었다.
'''