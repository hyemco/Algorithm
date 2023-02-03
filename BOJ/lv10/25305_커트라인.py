n, k = map(int, input().split())
students = list(map(int, input().split()))
print(sorted(students)[n - k])