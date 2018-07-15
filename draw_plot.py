# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 14:16:36 2018

@author: yaliang

E-mail:zyl731003407@qq.com
"""

def draw_violin(cell_line, hotspots, row=1, column=2, *file_tuple):

    import matplotlib.pyplot as plt
    import numpy as np

    def adjacent_values(vals, q1, q3):
        upper_adjacent_value = q3 + (q3 - q1) * 1.5
        upper_adjacent_value = np.clip(upper_adjacent_value, q3, vals[-1])

        lower_adjacent_value = q1 - (q3 - q1) * 1.5
        lower_adjacent_value = np.clip(lower_adjacent_value, vals[0], q1)
        return lower_adjacent_value, upper_adjacent_value

    def set_axis_style(ax, labels):
        ax.get_xaxis().set_tick_params(direction='out')
        ax.xaxis.set_ticks_position('bottom')
        ax.set_xticks(np.arange(1, len(labels) + 1))
        ax.set_xticklabels(labels)
        ax.set_xlim(0.25, len(labels) + 0.75)
        #ax.set_xlabel('Sample name')


    file_tuple = (
            '%s_0_%s_1000_10000.txt' % (cell_line, hotspots),
            '%s_1_%s_1000_10000.txt' % (cell_line, hotspots),
            )

    fig = plt.figure(figsize=(16, 9))

    fig_data = []
    for level, avg_file in enumerate(file_tuple):
        with open(avg_file, 'r') as infil:
                    data = [[] for i in range(3)]
                    for line in infil:
                        line = line.rstrip().split()
                        for i in xrange(len(line)):
                            data[i].append(float(line[i]))
                    fig_data.append(data)

    for data in fig_data:
        ax2 = fig.add_subplot(row, column, fig_data.index(data)+1)
        if fig_data.index(data) == 0 or fig_data.index(data) == 3:
            # set ylabel only for left plot
            ax2.set_ylabel('density')
        # set title for every plot
        ax2.set_title('%s %s %s' % (
         cell_line, fig_data.index(data), hotspots))

        try:
            parts = ax2.violinplot(
                    data, showmeans=False, showmedians=False,
                    showextrema=False)
        except BaseException:
            continue

        for pc in parts['bodies']:
            pc.set_facecolor('#D43F3A')
            pc.set_edgecolor('black')
            pc.set_alpha(1)

        quartile1, medians, quartile3 = np.percentile(
         data, [25, 50, 75], axis=1)

        inds = np.arange(1, len(medians) + 1)
        ax2.scatter(inds, medians, marker='o', color='white', s=30, zorder=3)
        ax2.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)

        # set style for the axes
        labels = ['boundary', 'nonboundary', 'population']
        set_axis_style(ax2, labels)
        plt.subplots_adjust(left=0.05, bottom=0.075, right=0.95, top=0.925,
         wspace=0.15, hspace=0.25)
        # plt.show()
    plt.savefig('%s %s density.png' % (cell_line, hotspots))

draw_violin('total', 'cancer_gene')
