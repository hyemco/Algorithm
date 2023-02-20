def enqueue(data):
    global rear
    queue[rear] = data
    rear = (rear + 1) % 8


def dequeue():
    global front
    front = (front + 1) % 8
    return queue[front - 1]


for _ in range(1, 11):
    tc = int(input())
    queue = list(map(int, input().split()))

    i = 1
    front, rear, cnt = 0, 0, 0
    while True:
        if i > 5:
            i = 1
        num = dequeue() - i
        if num <= 0:
            enqueue(0)
            rear += 1
            break
        enqueue(num)
        i += 1
        cnt += 1
    print(f'#{tc}', *queue[(cnt + 1) % 8:8], *queue[0:(cnt + 1) % 8])