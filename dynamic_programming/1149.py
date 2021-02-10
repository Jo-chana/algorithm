from sys import stdin

data = [list(map(int, stdin.readline().split())) for _ in range(int(stdin.readline()))]
cost = data[0]

for idx, d in enumerate(data):
	if idx == 0:
		continue
	score = [0, 0, 0]
	for i in range(3):
		score[i] = min(d[i] + cost[(i+1) % 3], d[i] + cost[(i+2) % 3])
	cost = score


print(min(cost))


'''
	문제 분류는 다이나믹 프로그래밍. 반복문 상에서 지속적으로 갱신되는 정답 배열을 이용해 메모이징 하여 해결하였다.
	원래 재귀함수를 가장 먼저 떠올렸으나 메모이징 아이디어가 생각이 잘 나지 않아 위 방식으로 풀었는데, 추후 다른
	해결 방안에 대해서도 공부해야겠다.
'''