cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']
cap3 = ['F', 'F', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']


def pleaseConformOnepass(caps):
    caps = caps + [caps[0]]
    start = 0
    cnt = 0
    for i in range(1, len(caps)):
        if caps[i] != caps[i - 1]:
            if caps[i] != caps[0]:
                print()
            else:
                if cnt == 1:
                    print(f'People at positions {i} flip your caps!.')
                else:
                    print(f' through {i - 1} flip your caps!')


if __name__ == '__main__':
    pleaseConformOnepass(cap1)
    print()
    pleaseConformOnepass(cap2)
    print()
    pleaseConformOnepass(cap3)
