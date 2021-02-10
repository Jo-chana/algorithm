from sys import stdin

In = stdin.readline
N = int(In())
data = [int(In()) for _ in range(N)]
memo = [[0, 0] for _ in range(N)]

if N == 1:
	print(data[0])
	exit()


def dp(step, seq):
	if memo[step][seq] > 0:
		return True
	if step == N - 1:
		memo[step][seq] = data[step]
		return True
	if step > N - 1:
		return False
	s1, s2 = 0, 0
	if seq == 0 and dp(step+1, 1):
		s1 = memo[step+1][1] + data[step]
	if step < N - 2 and dp(step+2, 0):
		s2 = memo[step+2][0] + data[step]
	if s1 == 0 and s2 == 0:
		return False
	memo[step][seq] = max(s1, s2)
	return True


[dp(i, 0) for i in range(2)]
print(max(memo[0][0], memo[1][0]))
'''
	계단오르기 동적계획법 문제. 처음 문제 이해를 잘못해서 풀이가 조금 오래 걸렸다.
	또한 N == 1인 경우를 고려하지 않아 채점 마지막에 IndexError 가 발생하여 
	코드 상단에 예외 처리하였다.
'''