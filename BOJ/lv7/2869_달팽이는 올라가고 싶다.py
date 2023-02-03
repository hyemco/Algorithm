up, down, top = map(int, input().split())

day = (top - down) / (up - down)
if day == (top - down) // (up - down):
    print(int(day))
else:
    print(int(day) + 1)