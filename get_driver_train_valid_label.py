#!/usr/bin/env python2
#coding:utf-8


import os
import random

if __name__ == '__main__':

    p = ['p002', 'p012', 'p014', 'p015', 'p016', 'p021', 'p022', 'p024', 'p026', 'p035', 'p039', 'p041', 'p042', 'p045',
         'p047', 'p049', 'p050', 'p051', 'p052', 'p056', 'p061', 'p064', 'p066', 'p072', 'p075', 'p081']
    random.shuffle(p)
    valid = p[0:3]
    print valid

    f = open('./driver_imgs_list.csv')
    drivers = f.readlines()[1:]
    f.close()
    path_train = []
    path_valid = []
    for i in drivers:
        person, label, img = i.split(',')
        if person in valid:
            path_valid.append(['train/'+label+'/'+img[:-1],label[1:]])
        else:
            path_train.append(['train/'+label+'/'+img[:-1],label[1:]])

    f = open('./train.txt','w')
    random.shuffle(path_train)
    for i in path_train:
        f.write(i[0])
        f.write(' ')
        f.write(i[1])
        f.write('\n')
    f.close()

    f = open('./valid.txt','w')
    random.shuffle(path_valid)
    for i in path_valid:
        f.write(i[0])
        f.write(' ')
        f.write(i[1])
        f.write('\n')
    f.close()






