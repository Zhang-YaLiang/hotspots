# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 08:55:14 2018

@author: yaliang

E-mail:zyl731003407@qq.com
"""

# import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

cell_line = 'total'
category = 'haDHS'
# category_name = 'hotspots'
total_times = 1000
cycles = 10000
# level = 0
path = 'D:\python\work\second semester\statistics\%s\%s' % (
 category, cell_line)
#==============================================================================
# singlefile = path+'\%s_%s_%s_%s_%s.txt' % (
#  cell_line, level, category, total_times, cycles)
#==============================================================================
density_file_tuple = (
 path+'\%s_0_%s_%s_%s.txt' % (cell_line, category, total_times, cycles),
 path+'\%s_1_%s_%s_%s.txt' % (cell_line, category, total_times, cycles)
# =============================================================================
#  path+'\%s_2_%s_%s_%s.txt' % (cell_line, category, total_times, cycles),
#  path+'\%s_3_%s_%s_%s.txt' % (cell_line, category, total_times, cycles),
#  path+'\%s_4_%s_%s_%s.txt' % (cell_line, category, total_times, cycles)
# =============================================================================
 )
with open('%s_%s_testing_result.txt' % (cell_line, category), 'w') as test:
    for level, singlefile in enumerate(density_file_tuple):
        with open(singlefile, 'r') as density:
            boundary_list = []
            nonboundary_list = []
            population_list = []
            for line in density:
                line = line.split()
                boundary_list.append(float(line[0]))
                nonboundary_list.append(float(line[1]))
                population_list.append(float(line[2]))
            group = np.array([boundary_list, nonboundary_list, population_list])

        ttest_boundary_nonboundary = stats.ttest_ind(group[0], group[1])
        ttest_boundary_population = stats.ttest_ind(group[0], group[2])
        ttest_nonboundary_population = stats.ttest_ind(group[2], group[1])

        wilcox_boundary_nonboundary = stats.ranksums(group[0], group[1])
        wilcox_boundary_population = stats.ranksums(group[0], group[2])
        wilcox_nonboundary_population = stats.ranksums(group[2], group[1])

        test.write('level:%s\n' % level)
        test.write('ttest_boundary_nonboundary'+'\t'+'\t'.join(
         [str(i) for i in ttest_boundary_nonboundary])+'\n')
        test.write('ttest_boundary_population'+'\t'+'\t'.join(
         [str(i) for i in ttest_boundary_population])+'\n')
        test.write('ttest_nonboundary_population'+'\t'+'\t'.join(
         [str(i) for i in ttest_nonboundary_population])+'\n')
        test.write('wilcox_boundary_nonboundary'+'\t'+'\t'.join(
         [str(i) for i in wilcox_boundary_nonboundary])+'\n')
        test.write('wilcox_boundary_population'+'\t'+'\t'.join(
         [str(i) for i in wilcox_boundary_population])+'\n')
        test.write('wilcox_nonboundary_population'+'\t'+'\t'.join(
         [str(i) for i in wilcox_nonboundary_population])+'\n')


#==============================================================================
# with open('test.txt','w') as test:
#     ks_list = []
#     bart_list = []
#     t_list = [[],[],[]]
#     wilcox_list = []
#     size = 100
#     a = 0.05
#     adjust_a = 0.05/100
#     t_null = 0
#     reject = 0
#     t_pp_list = []
#     for num in xrange(100):
#         boundary = group[0][size*num:size*(num+1)]
#         boundary_mean = np.mean(group[0][size*num:size*(num+1)])
#         boundary_std = np.std(group[0][size*num:size*(num+1)])
#
#         nonboundary = group[1][size*num:size*(num+1)]
#         nonboundary_mean = np.mean(group[1][size*num:size*(num+1)])
#         nonboundary_std = np.std(group[1][size*num:size*(num+1)])
#
#         population = group[2][size*num:size*(num+1)]
#         population_mean = np.mean(group[2][size*num:size*(num+1)])
#         population_std = np.std(group[2][size*num:size*(num+1)])
#
#         #
#         population_2 = group[2][size*(num+1):size*(num+2)]
#         bart_pp = stats.bartlett(population, population_2)
#         if bart_pp[1] > a:
#             t_pp = stats.ttest_ind(population, population_2)
#             if t_pp[1] > adjust_a:
#                 print '%d population population_2 %f' % (num, t_pp[1])
#             else:
#                 print 'pp has no diff'
#         else:
#             t_pp = stats.ttest_ind(population, population_2, equal_var=False)
#             if t_pp[1] > adjust_a:
#                 print '%d population population_2 %f' % (num, t_pp[1])
#             else:
#                 print 'pp has no diff,P-value: %f' % t_pp[1]
#         t_pp_list.append(t_pp[1])
#
#         ks_01 = stats.kstest(boundary, 'norm', (boundary_mean, boundary_std))
#         ks_12 = stats.kstest(nonboundary, 'norm', (nonboundary_mean, nonboundary_std))
#         ks_20 = stats.kstest(population, 'norm', (population_mean, population_std))
#
#         ks_list.append([ks_01[1], ks_12[1], ks_20[1]])
#
#         wilcox_01 = stats.ranksums(boundary, nonboundary)
#         wilcox_12 = stats.ranksums(nonboundary, population)
#         wilcox_20 = stats.ranksums(population, boundary)
#
#         wilcox_list.append([wilcox_01[1], wilcox_12[1], wilcox_20[1]])
#
#         if ks_list[num][0] < a or ks_list[num][1] < a or ks_list[num][2] < a:
#                 print num
#         else:
#             # boundary nonboundary
#             bart_01 = stats.bartlett(boundary, nonboundary)
#             if bart_01[1] > a:
#                 t_01 = stats.ttest_ind(boundary, nonboundary)
#                 if t_01[1] > adjust_a:
#                     print '%d boundary nonboundary %f' % (num, t_01[1])
#                     t_null += 1
#                 else:
#                      reject += 1
#
#             else:
#                 t_01 = stats.ttest_ind(boundary, nonboundary, equal_var=False)
#                 if t_01[1] > adjust_a:
#                     print '%d boundary nonboundary %f' % (num, t_01[1])
#                     t_null += 1
#                 else:
#                     reject += 1
#
# #==============================================================================
# #                 print ('%d boundary_nonboundary \n' % num,
# #                 'bartlett p-value:%1.130f' % bart_01[1],
# #                 't test p-value:%1.130f' % t_01[1])
# #==============================================================================
#
#             # nonboundary population
#             bart_12 = stats.bartlett(nonboundary, population)
#             if bart_12[1] > a:
#                 t_12 = stats.ttest_ind(nonboundary, population)
#                 if t_12[1] > adjust_a:
#                     # print '%d nonboundary population %f' % (num, t_12[1])
#                     t_null += 1
#                 else:
#                     reject += 1
#             else:
#                 t_12 = stats.ttest_ind(nonboundary, population, equal_var=False)
#                 if t_12[1] > adjust_a:
#                     # print '%d nonboundary population %f' % (num, t_12[1])
#                     t_null += 1
#                 else:
#                     reject += 1
#
#             # boundary  population
#             bart_20 = stats.bartlett(population, boundary)
#             if bart_20[1] > a:
#                 t_20 = stats.ttest_ind(population, boundary)
#                 if t_20[1] > adjust_a:
#                     print '%d boundary population %f' % (num, t_20[1])
#                     t_null += 1
#                 else:
#                     reject += 1
#
#             else:
#                 t_20 = stats.ttest_ind(population, boundary, equal_var=False)
#                 if t_20[1] > adjust_a:
#                     print '%d boundary population %f' % (num, t_20[1])
#                     t_null += 1
#                 else:
#                     reject += 1
#
#             bart_list.append([bart_01[1], bart_12[1], bart_20[1]])
#             t_list[0].append(t_01[1])
#             t_list[1].append(t_12[1])
#             t_list[2].append(t_20[1])
#
# wilcox_array = np.array(wilcox_list)
# t_array = np.array(t_list)
#
# t_pp_list.sort()
# print min(t_pp_list)
# plt.hist(t_pp_list[:-1], 50)
# plt.xlabel('p-value')
# # plt.xlim(0.0, 1)
# plt.ylim(0, 10)
# plt.ylabel('Frequency')
# plt.title('Frequence of P-value')
#
# plt.hist(t_list[0], 20)
# plt.xlabel('p-value')
# # plt.xlim(0.0,0.1)
# # plt.ylim(0,100)
# plt.ylabel('Frequency')
# plt.title('Frequence of P-value')
# plt.show()
#==============================================================================
