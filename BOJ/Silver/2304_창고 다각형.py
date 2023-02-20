N = int(input())
pillar = [0 for _ in range(1001)]
m = 0
m_idx = 0
for _ in range(N):
    L, H = map(int, input().split())
    pillar[L] = H
    if m < H:
        m_idx = L
        m = H

max_pillar = 0
ans = 0
for i in range(m_idx+1):
    max_pillar = max(max_pillar, pillar[i])
    ans += max_pillar

max_pillar = 0
for i in range(1000, m_idx, -1):
    max_pillar = max(max_pillar, pillar[i])
    ans += max_pillar
print(ans)