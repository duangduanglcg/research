from clu.metrics import *
import time


def hierarchicalClustering(data_file):
    sequences = sequences_process(data_file)
    clusters = []
    for i in range(len(sequences)):
        tmp1 = []
        tmp1.append(sequences[i])
        clusters.append(tmp1)

    groupNum = len(clusters)
    finalGroupNum = int(groupNum * 0.1)
    distance = []
    # startt = time.time()
    while groupNum > finalGroupNum:
        number = 1
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                # dis = compute_averageLinkage(clusters[i], clusters[j])
                # dis = compute_singleLinkage(clusters[i], clusters[j])
                dis = compute_completeLinkage(clusters[i], clusters[j])
                if dis <= number:
                    number = dis
                    tmp1 = clusters[i]
                    tmp2 = clusters[j]
                    tmp = clusters[i] + clusters[j]
        distance.append(number)
        clusters.remove(tmp1)
        clusters.remove(tmp2)
        clusters.append(tmp)
        groupNum -= 1
    # starte = time.time()
    return clusters
    # return starte-startt

def distanceCP(data_file):
    sequences = sequences_process(data_file)
    clusters = []
    for i in range(len(sequences)):
        tmp1 = []
        tmp1.append(sequences[i])
        clusters.append(tmp1)

    groupNum = len(clusters)
    finalGroupNum = int(groupNum * 0.1)
    distance = []
    while groupNum > finalGroupNum:
        number = 1
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                # dis = compute_averageLinkage(clusters[i], clusters[j])
                # dis = compute_singleLinkage(clusters[i], clusters[j])
                dis = compute_completeLinkage(clusters[i], clusters[j])
                if dis <= number:
                    number = dis
                    tmp1 = clusters[i]
                    tmp2 = clusters[j]
                    tmp = clusters[i] + clusters[j]
        distance.append(number)
        clusters.remove(tmp1)
        clusters.remove(tmp2)
        clusters.append(tmp)
        groupNum -= 1
    return distance



# file_name = 'camel'
# result_create(file_name)
# output = sys.stdout
# output_file = open('D:/develop/python_workspace/clu/result/' + file_name + '.txt', 'w')
# sys.stdout = output_file
# print(starte - startt, file=output_file)
# print(similarity, file=output_file)
# print(clusters , file=output_file)
# output_file.close()



