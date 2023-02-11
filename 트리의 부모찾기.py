from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
tree = dict()
for i in range(1,N+1):
	tree[i] = []
for _ in range(N-1):
	n1,n2 = map(int,input().split())
	tree[n1].append(n2)
	tree[n2].append(n1)
queue = deque([1])
parent = [0] * (N+1)
while queue:
	k = queue.popleft()
	for i in tree[k]:
		if parent[i] == 0 and i != 1:
			parent[i] = k
			queue.append(i)
for i in range(2,N+1):
	print(parent[i])