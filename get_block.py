# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 20:55:17 2018

@author: yaliang

E-mail:1637788l@gmail.com

"""

def get_lane_length_D(area):

    lane_length_D={}
    for lane_head,lane_value in area.items():
        lane_length_D[lane_head]=sum(
                [region[-1]-region[0] for region in lane_value])
    return lane_length_D

def random_lane(lane_length_D):
    '''
    # 随机获取某条lane
    以1到总长范围内随机得到一个随机数值，
    使用每条lane的长度作为该lane的权重，以随机获取某一条lane
    lane长度逐步相加，直到加完某一个lane的长度之和超过随机数时，则随机取得该lane
    '''

    import random

    random_site = random.randint(1,
        sum([value for value in lane_length_D.values()]))
    lane_length_sum = 0
    for lane_index, lane_length in lane_length_D.items():
        lane_length_sum += lane_length
        if random_site <= lane_length_sum:
            break
    return lane_index


def random_region(area, lane_n):
    '''
    获取该lane上的非特定区域的区域长度
    作为每个非特定区域的随机权重
    第四步在1到非特定区域总长范围得到一个随机数值
    region长度逐步相加，知道加完某一个非特定区域的长度之和超过随机数时，
    则随机取得该非特定区域
    '''

    import random

    region_length_L = [
     region[-1]-region[0] for region in area[lane_n]]

    random_region_site = random.randint(
     1, sum(region_length_L))
    region_length_sum = 0
    for region_index, region_length in enumerate(
     region_length_L):
        region_length_sum += region_length
        if random_region_site <= region_length_sum:
            break

    return region_index

def random_block(area, lane_n, region_n, length):
    '''
    在选择的lane的region中随机选择某一点作为region上的随机点
    region长减去区域的长度是为了防止超出上边界
    这么做也是同时为了确保每一段区域都是等概率被取到
    如果length==0，则获取特定区域
    如果length!=0则获取length长度的非特定区域或全局区域
    '''

    import random

    if length!=0:
        random_site = random.randint(area[lane_n][region_n][0],
                 area[lane_n][region_n][1]-length)
        random_block=(random_site, random_site + length)

        return random_block

    else:
        random_block=(area[lane_n][region_n][0],area[lane_n][region_n][1])

        return random_block

def write_block_in_D(lane_n, random_block_D, random_block):
    '''
    将random region写入字典
    '''
    if lane_n not in random_block_D:
        # 第一次选择某个lane
        random_block_D[lane_n]=[random_block]
    else:
        # 非第一次选择某个lane
        random_block_D[lane_n].append(random_block)

    return random_block_D



def random_block_D(random_times, area, total_length=0):
    '''
    get random nonspecial region 获取随机的特定区域
    随机次数由random_times给定
    选取的长度由length、random_times共同确定
    随机区域由area给定
    '''
    random_block_D = {}
    count = 1
    length=int(total_length/random_times)
    while count <= random_times:
        # 第一步获取lane的长度
        lane_length_D=get_lane_length_D(area)

        # 第二步随机获取一条lane
        lane_n=random_lane(lane_length_D)

        # 第三步随机获取一个region
        region_n=random_region(area, lane_n)

        # 判断是获取特定区域还是非特定区域和全体区域
        if area[lane_n][region_n][1]-area[lane_n][region_n][0]>length:
            # 第四步随机获取一个block
            block_n=random_block(area,lane_n, region_n, length)

            # 第五步将random block写入字典
            random_block_D=write_block_in_D(
                lane_n,random_block_D,block_n)

            #计数
            count+=1
        else:
            continue

    return random_block_D

def total_random_length(random_block_D):
    '''
    获取随机选取的特定区域的总长，
    在非特定区域和全局区域选取相同的长度
    以确保三者之间具有可比性
    后续计算也方便
    '''
    total_length=0
    for lane_value in random_block_D.values():
        for region in lane_value:
            total_length+=region[-1]-region[0]

    return total_length















