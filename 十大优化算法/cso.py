import numpy as np
import pandas as pd
from benchmark import Benchmark
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
    def __init__(self, m=50, p=40, d=20, lb=-100, ub=100, f=1):
        self.G = 10
        self.rpercent = 0.2
        self.hpercent = 0.6
        self.mpercent = 0.1
        self.m = m
        self.pop = p
        self.dim = d
        self.rNum = int(p * self.rpercent)
        self.hNum = int(p * self.hpercent)
        self.cNum = self.pop - self.rNum - self.hNum
        self.mNum = int(p * self.mpercent)
        self.lowb = lb
        self.upb = ub
        self.fit = np.zeros((self.pop, 10))
        self.pfit = np.zeros((self.pop, 10))
        self.gfit = np.zeros(10)
        self.gbest = np.zeros((10, self.dim))
        xi = np.zeros(self.dim)
        # 初始化鸡的位置
        self.x = pd.DataFrame(-1 + 2 *
                              np.random.rand(self.pop, self.dim)) * 100
        test = Benchmark(self.dim)
        for i in np.arange(self.pop):  # 初始化鸡的适应度
            xi = self.x.iloc[i]
            self.fit[i] = test.Fitness(xi)
        self.p_fit = pd.DataFrame(self.fit)
        self.pfit = self.p_fit         # 初始化更新前适应度
        self.gfit = self.p_fit.min()   # 初始化全局最优适应度
        self.ind = self.p_fit.idxmin()
        self.gbest = self.x.iloc[self.ind]  # 初始化全局最优位置

    def runcso(self):

        for t in np.arange(1):
            for func in np.arange(10):      # 分别求十个测试函数的
                func_pfit = self.pfit[func]
                func_gfit = self.gfit[func]
                func_gbest = self.gbest[func]
                if(t % self.G == 0):
                    mate = np.array([])             # 小组中公鸡标签
                    mother = np.array([])           # 小组中有小鸡的母鸡标签
                    motherlib = np.array([])        # 成为母亲母鸡的标签

                    func_pfit = func_pfit.sort_values()
                    chick = func_pfit[self.rNum + self.hNum:]

                    for i in np.arange(self.hNum):  # 将母鸡与公鸡随机进行配对
                        mate = np.append(mate, np.random.randint(0, self.rNum))

                    i = 0
                    while(i < self.mNum):  # 随机选取mNum个可能成为母亲的母鸡
                        ml = np.random.randint(
                            self.rNum, self.rNum + self.hNum)
                        if(ml not in motherlib):
                            motherlib = np.append(motherlib, ml)
                            i = i + 1

                    for i in np.arange(self.cNum):
                        mother = np.append(
                            mother, motherlib[np.random.randint(0, self.mNum)])

                    print(mate)
                    print(mother)
                    print(motherlib)
