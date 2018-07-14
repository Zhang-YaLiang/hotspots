# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 16:43:57 2018

@author: yaliang

E-mail:1637788l@gmail.com

"""


def hotspots_D(hotspots_filename):
    with open(hotspots_filename, 'r') as hotspotsfile:
        hotspots_D = {}
        for hotspot in hotspotsfile:
            hotspot_L = hotspot.rstrip().split()
            if hotspot_L[0] in hotspots_D:
                hotspots_D[hotspot_L[0]].append((int(hotspot_L[1]),
                            int(hotspot_L[2])))
            else:
                hotspots_D[hotspot_L[0]]=[(int(hotspot_L[1]),
                  int(hotspot_L[2]))]
    return hotspots_D

def get_counts(random_D, hotspots_D):
    lane_counts_hotspots_D = {}
    for lane_head, lane_value in random_D.items():
        lane_hotspot_count = 0
        for location in random_D[lane_head]:
            for hotspot in lane_value:
                if location[0] <= hotspot[1] and hotspot[0] <= location[1]:
                    lane_hotspot_count += 1
        lane_counts_hotspots_D[lane_head]=lane_hotspot_count
    return lane_counts_hotspots_D


