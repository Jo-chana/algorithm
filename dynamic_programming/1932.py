from sys import stdin

data = [list(map(int, stdin.readline().split())) for _ in range(int(stdin.readline()))]
data.reverse()

for idx, d in enumerate(data):
	if idx == 0:
		continue
	for i in range(len(d)):
		d[i] = max(d[i] + data[idx-1][i], d[i] + data[idx-1][i+1])


print(data[-1][0])


'''
	가장 하위 케이스(리프) 부터 올라가면서 배열을 갱신하는 메모이징 기법을 사용하면 쉽게 풀 수 있는 문제였다.
'''