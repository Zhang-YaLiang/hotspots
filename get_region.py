# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 20:55:30 2018

@author: yaliang

E-mail:1637788l@gmail.com

"""



#def get_wh

def special_region(special_region_filename):
    '''
    输入文件格式：
        lane1 a b
        lane1 c d
    其中a<b,c<d,b<c
    eg:
        chr1 20000 50000
        chr1 60000 90000
    输出为字典格式：
    chr1:[(20000,50000),(60000,90000),...]
    chr2:[...]
    ...
    '''
    with open(special_region_filename, 'r') as special_regions:
        region_D = {}   #存储特定区域(special region)
        for region in special_regions:
            region_L = region.rstrip().split()
            if region_L[0] in region_D: #
                region_D[region_L[0]].append((int(region_L[1]),
                            int(region_L[2])))
            else:
                region_D[region_L[0]]=[(int(region_L[1]),
                  int(region_L[2]))]
        for region in region_D.values():# sort for next step
            region.sort()
    return region_D

def global_region(global_file):
    '''
    输入文件格式：
        lane1 x
        lane2 y
    其中x为lane1的size
    eg:
        chr1 249250621
        chr2 243199373
    输出为字典格式：
    chr1:[(0,249250621)]
    chr2:[(0,243199373)]
    ...
    '''
    with open(global_file,'r') as g_f:
        global_D={} #eg,save as dict by chromosome
        for lane in g_f:
            lane_L=lane.rstrip().split()
            global_D[lane_L[0]]=[(0,int(lane_L[1]))]
    return global_D

def nonspecial_region(global_D,region_D):
    '''
    输入为get_global和get_special_region的输出
    即special region和global region的两个字典
    输出为nonspecial region的字典格式：
    chr1:[(0,20000),(50000,60000),...]
    chr2:[...]
    ...
    '''
    nonspecial_region={}
    for lane_header in global_D:
        nonspecial_region[lane_header]=[] # 直接创建空的列表
        if lane_header not in region_D:
            '''
            如果没有任何region在某个lane里面的话，直接将整个lane变为nonspecial region
            '''
            nonspecial_region[lane_header].append(global_D[lane_header][-1])
        else:
            '''
            如果有region在lane里面的话，就按照：
                lane下界          第一个region起始位置
                第一个region终止位置   第二个region起始位置
                ...
                最后一个region终止位置 lane上界
            的形式来提取nonspecial region
            '''
            if region_D[lane_header][0][0]>global_D[lane_header][0][0]:
                '''
                确定某个lane中的第一个区域的起始位置是否大于下界，
                大于下界说明下界和起始位置之间有gap
                小于下界说明越界
                等于下界说明既没有越界也没有gap
                '''
                nonspecial_region[lane_header].append((0,
                                 region_D[lane_header][0][0]))
            elif region_D[lane_header][0][0]==global_D[lane_header][0][0]:
                pass
            else:
                raise Exception("Out of lower bounds: %s %d > %d",
                                lane_header, region_D[lane_header][0][0],
                                global_D[lane_header][0][0]
                                )
            #添加中间的nonspecial region
            for index in range(len(region_D[lane_header])-1):
                nonspecial_region[lane_header].append(
                 (region_D[lane_header][index][1],
                  region_D[lane_header][index+1][0]))

            if region_D[lane_header][-1][-1]<global_D[lane_header][0][-1]:
                '''
                在确定完下界的情况以及添加完中间的nonspecial region之后考虑上界的情况
                确定某个lane中最后一个区域的终止是否小于上界，
                小于上界说明上界和终止位置之间有gap
                大于上界说明越界
                等于上界说明既没有越界也没有gap
                '''
                nonspecial_region[lane_header].append(
                        (region_D[lane_header][-1][1],
                          global_D[lane_header][0][-1]))

            elif region_D[lane_header][-1][-1]==global_D[lane_header][0][-1]:
                pass
# =============================================================================
#             else:#在TAD boundary的情况下很容易有越过上界的情形，所以注释掉
#                 raise Exception("Out of upper bounds",
#                                 lane_header, global_D[lane_header][1],
#                                 region_D[lane_header][-1][1])
# =============================================================================

    return nonspecial_region


