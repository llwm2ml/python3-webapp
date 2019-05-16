def aab():
    from collections import deque
    q = deque([1, 0])
    while True:
        while True:
            item = q.popleft()
            q.append(item + q[0])
            if not q[0]:
                break
        q.append(0)
        yield (list(q)[1:-1])