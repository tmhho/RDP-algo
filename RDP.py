def dist(p,q,r):
    tmp = [p[0]-q[0],p[1]-q[1]]
    tmp2 = [q[0]-r[0],q[1]-r[1]]
    return abs(tmp2[0]*tmp[1] - tmp2[1]*tmp[0])

def RDP(PointList, eps):
    dmax = 0
    index = 0
    end = len(PointList)-1
    for i in range(1,end):
        d = dist(PointList[i], Line(PointList[0], PointList[end])) 
        if (d > dmax):
            index = i
            dmax = d
    
    ResultList = []
    
    if (dmax > eps):
        recResults1 = RDP(PointList[:index+1], eps)
        recResults2 = RDP(PointList[index:], eps)

        ResultList = recResults1 + recResults2[1:]
    else:
        ResultList = [PointList[0], PointList[end]]
    
    return ResultList
end
