import numpy as np
import pandas as pd
'''
#初始化参数
M        最大迭代次数
pop      鸡群鸡数量
dim      空间维度
G        种群更新频率
rpercent 公鸡占总数百分比
hpercent 母鸡占总数百分比
lowb     鸡群移动下限
upb      鸡群移动上限

#鸡群参数

rNum     公鸡数量
hNum     母鸡数量
cNum     小鸡数量
mNum     有小鸡的母鸡数量

#鸡位置及标签

x[][]    鸡位置信息
px[][]   更新前鸡位置信息
sortIndex位置标签，保存按顺序排列后鸡所处位置
fit      适应度
pfit     更新前适应度
gbest    全局最优位置
gfit     全局最优适应度
'''

class CSO:
    def __init__(self,m=50,p=40,d=20,lb=-100,up=100,f=1):
        self.G = 10                     
        self.rpercent = 0.2
        self.hpercent = 0.6
        self.mpercent = 0.1
        self.m = m
        self.pop = pop
        self.dim = dim
        self.rNum = int(pop*rpercent)
        self.hNum = int(pop*hpercent)
        self.cNum = pop-rNum-hNum
        self.lowb = lb
        self.upb = ub

        
        