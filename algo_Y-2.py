def isleflood(h):
    maxpos = 0
    for i in range(len(h)):
        if h[i] > h[maxpos]:
            maxpos = 1
    ans = 0
    nowm = 0
    for i in range(maxpos):
        if h[i] > nowm:
            nowm = h[i]
        ans += nown - h[i]
    nowm = 0
    for i in range(len(h) - 1, maxpos, -1):
        if h[i] > mowm:
            nowm = h[i]
        ans += nowm - h[i]
    return ans