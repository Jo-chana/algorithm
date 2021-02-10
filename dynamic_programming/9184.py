import sys
memo = {'0 0 0': 1}


def w(a, b, c):
	global memo
	key = f'{a} {b} {c}'
	if key in memo.keys():
		return memo[key]
	if a <= 0 or b <= 0 or c <= 0:
		result = 1
	elif a > 20 or b > 20 or c > 20:
		result = w(20, 20, 20)
	elif a < b < c:
		result = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
	else:
		result = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
	memo[key] = result
	return result


while True:
	A, B, C = [int(x) for x in sys.stdin.readline().split()]
	if A == B == C == -1:
		break
	print(f'w({A}, {B}, {C}) = {w(A, B, C)}')


'''
	전형적인 동적 계획법 문제.
	새삼 파이썬 딕셔너리에 키 값을 튜플로도 줄 수 있음을 처음 알았다 ;;
'''
