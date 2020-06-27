sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12), (9, 10), (10, 11), (10, 12), (11, 12)]
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0), (8.0, 10.0), (9.0, 12.0),
          (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]
sched3 = [(6.0, 8.0, 2), (6.5, 12.0, 1), (6.5, 7.0, 2), (7.0, 8.0, 2), (7.5, 10.0, 3), (8.0, 9.0, 2), (8.0, 10.0, 1),
          (9.0, 12.0, 2), (9.5, 10.0, 4), (10.0, 11.0, 2), (10.0, 12.0, 3), (11.0, 12.0, 7)]


def bestTimeToPartySmart3(schedule):
    times = []
    for i in schedule:
        times.append((i[0], 's', i[2]))
        times.append((i[1], 'e', i[2]))
    times = sorted(times)
    cnt = 0
    ans = time = 0

    for t in times:
        if t[1] == 's':
            cnt += t[2]
        else:
            cnt -= t[2]
        if ans < cnt:
            ans = cnt
            time = t[0]

    print(f'Best time to attend the party is at {time} o\'clock : {ans} celebrities will be attending!')


if __name__ == '__main__':
    bestTimeToPartySmart3(sched3)
