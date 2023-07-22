import sys
input = sys.stdin.readline

n, m = map(int, input().split())
not_heard = set([input().strip() for _ in range(n)])
not_seen = set([input().strip() for _ in range(m)])

not_heard_seen = list(not_heard & not_seen)
not_heard_seen.sort()

print(len(not_heard_seen))

for n_h_s in not_heard_seen:
  print(n_h_s)