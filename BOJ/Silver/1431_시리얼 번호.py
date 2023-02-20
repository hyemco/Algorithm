N = int(input())
lst = [input() for _ in range(N)]
lst.sort()
lst.sort(key=lambda x: (len(x), sum(int(i) for i in x if i.isdigit())))

print(*lst, sep='\n')