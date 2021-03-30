from clu.HClustering import distanceCP
from clu.metrics import *


def innerClusterMaxDis(cluster):
    number = 0
    for i in range(len(cluster)):
        for j in range(i+1, len(cluster)):
            dis = sequence_sim(cluster[i], cluster[j])
            if dis > number:
                number = dis
    return number

def clusterCenter(cluster):
    cnt = 0
    length = (1 + len(cluster)) * len(cluster) / 2
    for i in range(len(cluster)):
        for j in range(i+1, len(cluster)):
            cnt += sequence_sim(cluster[i], cluster[j])
    return round(cnt/length, 4)


def computeCP(clusters):
    cnt = 0
    for i in range(len(clusters)):
        cnt += clusterCenter(clusters[i])
    return round(cnt/len(clusters), 4)


def computeCP1(file):
    tmp = distanceCP(file)
    cnt = 0
    sum = 0
    for i in range(len(tmp)):
        cnt += 1
        sum += tmp[i]
    print(sum / cnt)


def computeSP(clusters):
    cnt = 0
    length = (1 + len(clusters))*len(clusters)/2
    for i in range(len(clusters)):
        for j in range(i+1, len(clusters)):
            cnt += compute_averageLinkage(clusters[i], clusters[j])
    return round(cnt/length, 4)


def computeDVI(clusters):
    min = 1
    max = 0
    for i in range(len(clusters)):
        for j in range(i+1, len(clusters)):
            dis = compute_singleLinkage(clusters[i], clusters[j])
            if dis < min:
                min = dis
    for k in range(len(clusters)):
        dis = innerClusterMaxDis(clusters[k])
        if dis > max:
            max = dis
    return round(min/max, 4)




