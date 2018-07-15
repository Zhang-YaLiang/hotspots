# hotspots
calculate special region hotspots density

计算特定区域的热点密度

----------

# python脚本 #

## get_region.py ##

> 输入文件为特定区域的文件，相比较其他区域有其自身的特点
> 对应的还有全局区域的文件，一般来说，全局区域分为特定区域和非特定区域

- 函数

	- special_region()
> 	- 通过特定区域的文件获取字典格式的特定区域
> 	- 输入文件格式：
		> - lane1 a b
		> - lane1 c d
> 	- 其中a<b,c<d,b<c
> 	- eg:
		> - chr1 20000 50000
		> - chr1 60000 90000
> 	- 输出为字典格式：
		> - chr1:[(20000,50000),(60000,90000),...]
		> - chr2:[...]

	- global_region()
> 	- 通过全局区域的文件获取字典格式的全局区域
> 	- 输入文件格式：
		> - lane1 x
		> - lane2 y
> 	- 其中x为lane1的size
> 	- eg:
		> - chr1 249250621
		> - chr2 243199373
> 	- 输出为字典格式：
		> - chr1:[(0,249250621)]
		> - chr2:[(0,243199373)]
		> - ...

	- nonspecial_region()
> 	- 通过上面连个函数计算得到的特定区域字典和全局区域字典计算
> 	- 非特定区域的字典
> 	- 输入为get_global和get_special_region的输出
> 	- 即special region和global region的两个字典
> 	- 输出为nonspecial region的字典格式：
		> - chr1:[(0,20000),(50000,60000),...]
		> - chr2:[...]
		> - ...


## get_block.py ##
> 随机获取某区域上的部分区域用以后续计算

- 函数

	- random_block_D(random_times, area, total_length=0)
> 	- 在特定区域上，随机获取全部区域（暂时不能获取部分的特定区域，特定区域只能整体获取
> 	- 在非特定区域和全局区域上，随机获取部分区域，每一次获取的部分区域长度由total_length和random_times共同决定，总长度和特定区域随机获取的总长度一样。
> 	- 随机次数由random_times给定
> 	- 选取的长度由length、random_times共同确定
> 	- 随机区域由area给定

	- total_random_length()
> 	- 获取随机选取的特定区域的总长，在非特定区域和全局区域选取相同的长度，以确保三者之间具有可比性，后续计算也方便


## get_hotspots.py ##
> 从随机区域计算热点出现次数

- 函数

	- hotspots_D(hotspots_file)	
> 	- 从热点文件获取字典格式的热点数据
	
	- get_counts(random_D, hotspots_D)
> 	- 从随机区域获取热点出现次数


## avg_counts.py ##
> 计算特定区域、全局区域、非特定区域的热点平均出现次数

- 函数

	- Avg_Counts(s_region_file,global_file,hotspots_file,stat_length,random_times=1000)
> 	- s_region_filename:特定区域的文件
> 	- global_filename:全局区域的文件
> 	- hotspots_file:热点区域的文件
> 	- stat_length:每stat_length长度的热点区域密度
> 	- random_times：随机次数,默认1000次，即有放回的抽取1000次


如果只是计算，并且满足要求的话，
总共只需要使用一个Avg_Counts()函数就够了
需要输入三个文件并确定stat_length和random_times
下面讲一下输入的文件格式

----------


# 使用的文件 #
这里仅仅举一个例子：
现在打算观察是否重组热点在TAD boundary附近有附近情况。
可以计算重组热点（hotspots）在基因组的TAD boundary附近的密度，以及非TAD boundary附近的密度和全基因组上的密度。比较三者的情况即可。



> 特定区域的文件即TAD boundary的文件：
 

> - total-0-boundary.txt
> - 文件格式：
> - chr20	0	100000
> - chr20	5150000	5200000
> - chr20	5450000	5500000
> - ...

----------



> 基因组染色体大小文件：



> - chr_length_hg19.txt
> - 文件格式：
> - chr1	249250621
> - chr2	243199373
> - chr3	198022430
> - ...

----------


> 热点区域的文件：


> - DSB_hotspots.txt
> - 文件格式：
> - chr1	15497	18631
> - chr1	38426	40527
> - chr1	353112	354479
> - ...

----------
