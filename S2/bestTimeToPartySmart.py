sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12), (9, 10), (10, 11), (10, 12), (11, 12)]
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0), (8.0, 10.0), (9.0, 12.0),
          (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]


# def bestTimeToPartySmart(schedule):
#     times = []
#     for c in schedule:
#         times.append((c[0], 'start'))
#         times.append((c[1], 'end'))
#     sortList(times)
#     maxcount, time = chooseTime(times)
#
#     print(f'Best time to attend the party is at {time} o\'clock : {maxcount} celebrities will be attending!')
#
#
# def sortList(tList):
#     for ind in range(len(tList) - 1):
#         iSm = ind
#         for i in range(ind, len(tList)):
#             if tList[iSm][0] > tList[i][0]:
#                 iSm = i
#         tList[ind], tList[iSm] = tList[iSm], tList[ind]
#
#
# def chooseTime(times):
#     rcount = 0
#     maxcount = time = 0
#     for t in times:
#         if t[1] == 'start':
#             rcount += 1
#         else:
#             rcount -= 1
#         if rcount > maxcount:
#             maxcount = rcount
#             time = t[0]
#     return maxcount, time


def bestTimeToPartySmart(schedule):
    times = []
    for i in schedule:
        times.append((i[0], 's'))
        times.append((i[1], 'e'))
    times = sorted(times)
    print(times)
    cnt = 0
    ans = time = 0

    for t in times:
        if t[1] == 's':
            cnt += 1
        else:
            cnt -= 1
        if ans < cnt:
            ans = cnt
            time = t[0]
    print(f'Best time to attend the party is at {time} o\'clock : {ans} celebrities will be attending!')


if __name__ == '__main__':
    bestTimeToPartySmart(sched2)
