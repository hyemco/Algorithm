height = [int(input()) for _ in range(9)]
total_h = sum(height)
over_v = total_h - 100

for i in range(9):
    for j in range(i + 1, 9):
        if height[i] + height[j] == over_v:
            t1, t2 = height[i], height[j]
            height.remove(t1)
            height.remove(t2)
            break
    else:
        continue
    break

print(*sorted(height), sep='\n')