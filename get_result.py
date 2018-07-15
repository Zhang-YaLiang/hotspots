# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 20:53:50 2018

@author: yaliang

E-mail:1637788l@gmail.com

"""
import avg_counts

cell_line = 'total'
category = 'breakpoint'

path = 'D:\python\work\second semester\statistics\%s\%s' % (
     category, cell_line)

s_region_file_tuple = (path+'\%s-0-boundary.txt' % cell_line,
                       path+'\%s-1-boundary.txt' % cell_line)

whole_file='chr_length_hg19.txt'

hotspots_file = path+'\%s' % 'breakpoint.txt'

stat_length=100000

random_times = 1000

cycles=3

for level, s_region_file in enumerate(s_region_file_tuple):
    print 'level:', level
    with open(path+'\%s_%s_%s_%s_%s.txt' % (
     cell_line, level, category, random_times, cycles), 'w') as results:
        for times in range(cycles):
            print 'times:', times
            avg_result=avg_counts.Avg_Counts(
                    s_region_file,whole_file,hotspots_file,stat_length,random_times)
            results.write('\t'.join([str(round(i,3)) for i in avg_result])+'\n')


