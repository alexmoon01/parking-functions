def stat_encoding(pfs: set):
    mapping = dict()
    for pf in pfs:
        stat = ""
        for i in range(len(pf) - 1):
            if pf[i+1] > pf[i]:
                stat = stat + "A"
            elif pf[i+1] == pf[i]:
                stat = stat + "T"
            elif pf[i+1] < pf[i]:
                stat = stat + "D"
        mapping[pf] = stat
    return mapping


def count_zigzags(pfs: set):
    count = 0
    for pf in pfs:
        good = True
        if pf[1] <= pf[0]:
            good = False
        for i in range(len(pf) - 2):
            if (pf[i+2] - pf[i+1])*(pf[i+1]-pf[i]) >= 0:
                good = False
                break
        if good:
            count += 1
    return count


def AD_avoid(pfs: set):
    avoiders = set()
    for pf in pfs:
        good = True
        going_up = False
        for i in range(len(pf) - 1):
            if pf[i+1] > pf[i]:
                going_up = True
            if going_up and pf[i+1] < pf[i]:
                good = False
        if good:
            avoiders.add(pf)
    return avoiders


def DA_avoid(pfs: set):
    avoiders = set()
    for pf in pfs:
        good = True
        going_down = False
        for i in range(len(pf) - 1):
            if pf[i+1] < pf[i]:
                going_down = True
            if going_down and pf[i+1] > pf[i]:
                good = False
        if good:
            avoiders.add(pf)
    return avoiders
