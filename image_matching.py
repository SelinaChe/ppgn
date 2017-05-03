import os, sys
import numpy as np

print "Usage:	image_matching.py <train_feature> <train_label> <test_feature>"

train_fc8 = np.loadtxt(sys.argv[1])
train_labels = np.loadtxt(sys.argv[2])

test_fc8 = np.loadtxt(sys.argv[3])
#test_labels = np.loadtxt('feature_extraction/test_labels.txt')

def sort_by_value(value):
    items = value.items()
    backitems = [[v[1],v[0]] for v in items]
    backitems.sort()
    return [backitems[i][1] for i in range(0,len(backitems))]

def get_top_number(sorted_dic):
    count = 0
    for i in sorted_dic:
        count = count + 1
        #print str(i).split(',')[0].split('(')[1]
        print i, train_labels[int(str(i).split(',')[0].split('(')[1])]
        if count == 10:
            print '*************'
            break


#euclidean_distance
euclidean_distance = {}
for i in range(len(test_fc8)):
    for j in range(len(train_fc8)):
        difference = train_fc8[j] - test_fc8[i]
        euclidean = 0
        for one in difference:
            euclidean = euclidean + one*one
        euclidean_distance[j] = euclidean
    sorted_euclidean_distance =  sorted(euclidean_distance.items(), key=lambda d: d[1])
    get_top_number(sorted_euclidean_distance)


'''
#Hanmin distance
hanmin_distance = {}
for i in range(len(test_fc8)):
    for one in range(len(test_fc8[i])):
        if float(test_fc8[i][one]) < 0.5:
            test_fc8[i][one] = 0
        else:
            test_fc8[i][one] = 1
    for j in range(len(train_fc8)):
        for one in range(len(train_fc8[j])):
            if float(train_fc8[j][one]) < 0.5:
                train_fc8[j][one] = 0
            else:
                train_fc8[j][one] = 1
        #difference = train_fc8[j] - test_fc8[i]
        hanmin = 0
        for ii in range(len(train_fc8[j])):
            if train_fc8[j][ii] != test_fc8[i][ii]:
                hanmin = hanmin + 1
        hanmin_distance[j] = hanmin
    sorted_hanmin_distance = sorted(hanmin_distance.items(), key=lambda d: d[1])
    get_top_number(sorted_hanmin_distance)
'''
