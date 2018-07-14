# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 18:08:03 2018

@author: yaliang

E-mail:1637788l@gmail.com

"""

def Avg_Counts(s_region_file,global_file,hotspots_file,stat_length,random_times=1000):
    '''
    s_region_filename:特定区域的文件
    global_filename:全局区域的文件
    hotspots_file:热点区域的文件
    stat_length:每stat_length长度的热点区域密度
    random_times：随机次数,默认1000次，即有放回的抽取1000次
    '''
    import get_region
    import get_block
    import get_hotspots
    # 获取特定区域、全局区域、非特定区域字典
    s_region_D=get_region.special_region(s_region_file)

    global_D=get_region.global_region(global_file)

    nons_region_D=get_region.nonspecial_region(global_D,s_region_D)

    # 获取特定区域、全局区域、非特定区域的随机区块
    sr_ran_block=get_block.random_block_D(random_times,s_region_D)

    # 获取随机取random_times次的取得的总长
    total_length=get_block.total_random_length(sr_ran_block)

    global_ran_block=get_block.random_block_D(random_times,global_D,total_length)

    nonsr_ran_block=get_block.random_block_D(
            random_times,nons_region_D,total_length)

# =============================================================================
#     gr_total_length=get_block.total_random_length(global_ran_block)
#
#     nonsr_total_length=get_block.total_random_length(nonsr_ran_block)
#
#     print('random sr total length:',total_length)
#     print('random gr total length:',gr_total_length)
#     print('random nonsr total length:',nonsr_total_length)
# =============================================================================

    # 获取热点区域字典
    hotspots_D=get_hotspots.hotspots_D(hotspots_file)

    # 获取特定区域、全局区域、非特定区域的热点统计个数
    sr_counts_D=get_hotspots.get_counts(sr_ran_block,hotspots_D)

    global_counts_D=get_hotspots.get_counts(global_ran_block,hotspots_D)

    nonsr_counts_D=get_hotspots.get_counts(nonsr_ran_block,hotspots_D)

# =============================================================================
#     print('sr counts D:',sr_counts_D)
#     print('global counts D:',global_counts_D)
#     print('nonsr counts D:',nonsr_counts_D)
# =============================================================================

    # 获取特定区域、全局区域、非特定区域的每stat_length长度的热点平均数
    sr_total_counts=sum([counts for counts in sr_counts_D.values()])
    sr_avg_counts=1.0*sr_total_counts/total_length*stat_length

    global_total_counts=sum([counts for counts in global_counts_D.values()])
    global_avg_counts=1.0*global_total_counts/total_length*stat_length

    nons_total_counts=sum([counts for counts in nonsr_counts_D.values()])
    nonsr_avg_counts=1.0*nons_total_counts/total_length*stat_length

# =============================================================================
#     print('sr total counts:',sr_total_counts)
#     print('global total counts:',global_total_counts)
#     print('nonsr total counts:',nons_total_counts)
# =============================================================================

    return (sr_avg_counts,global_avg_counts,nonsr_avg_counts)





