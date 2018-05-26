import numpy as np
import pandas as pd
from benchmark import Benchmark
from matplotlib import pyplot as plt
'''
# 初始化参数
M        最大迭代次数
pop      鸡群鸡数量
dim      空间维度
G        种群更新频率
rpercent 公鸡占总数百分比
hpercent 母鸡占总数百分比
lowb     鸡群移动下限
upb      鸡群移动上限
f        测试函数索引

# 鸡群参数

rNum     公鸡数量
hNum     母鸡数量
cNum     小鸡数量
mNum     有小鸡的母鸡数量

# 鸡位置及标签

x[][]    鸡位置信息
px[][]   更新前鸡位置信息
sortIndex位置标签，保存按顺序排列后鸡所处位置
fit      适应度
pfit     更新前适应度
gbest    全局最优位置
gfit     全局最优适应度
'''


class CSO:
    def __init__(self, m=50, p=40, d=20, lb=-100, ub=100, f=7):
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
        self.fit = np.zeros(self.pop)
        self.pfit = np.zeros(self.pop)
        self.gbest = np.zeros(self.dim)
        self.f = f
        self.gfit_list = np.zeros(0)
        xi = np.zeros(self.dim)
        # 初始化鸡的位置
        self.x = pd.DataFrame(-1 + 2 *
                              np.random.rand(self.pop, self.dim)) * 100
        self.px = self.x

        self.test = Benchmark(self.dim, self.f)
        for i in np.arange(self.pop):  # 初始化鸡的适应度
            xi = self.x.iloc[i]
            self.fit[i] = self.test.Fitness(xi)

        self.pfit = pd.DataFrame(self.fit)    # 初始化更新前适应度
        self.gfit = self.pfit.min()   # 初始化全局最优适应度
        self.ind = self.pfit.idxmin()
        self.gbest = self.x.iloc[self.ind]  # 初始化全局最优位置
        # print(self.pfit)
        # print("初始化鸡的位置")
        # print(self.x)

    def runcso(self):
        for t in np.arange(self.m):

            self.px = self.x
            # func_gfit = self.gfit[func]
            # func_gbest = self.gbest[func]
            if(t % self.G == 0):
                mate = np.array([])             # 小组中公鸡标签
                mother = np.array([])           # 小组中有小鸡的母鸡标签
                motherlib = np.array([])        # 成为母亲母鸡的标签

                self.pfit = self.pfit.sort_values(by=0)
                tempIndex = self.pfit.index
                self.px = self.px.reindex(tempIndex)
                self.px.index = np.arange(self.pop)
                # print("排序后鸡的位置")
                # print(self.px)

                for i in np.arange(self.hNum):  # 将母鸡与公鸡随机进行配对
                    mate = np.append(mate, np.random.randint(0, self.rNum))

                i = 0
                while(i < self.mNum):  # 随机选取mNum个可能成为母亲的母鸡
                    ml = np.random.randint(
                        self.rNum, self.rNum + self.hNum)
                    if(ml not in motherlib):
                        motherlib = np.append(motherlib, ml)
                        i = i + 1

                for i in np.arange(self.cNum):  # 小鸡与母鸡配对
                    mother = np.append(
                        mother, motherlib[np.random.randint(0, self.mNum)])

            for i in np.arange(self.rNum):
                while(True):  # 求另外一只随机公鸡
                    anotherRooster = np.random.randint(0, self.rNum)
                    if (anotherRooster != i):
                        break
                if (self.pfit.iloc[anotherRooster][0] >= self.pfit.iloc[i][0]):  # 求tempSigma
                    tempSigma = 1.0
                else:
                    tempSigma = np.exp(
                        (self.pfit.iloc[anotherRooster][0] - self.pfit.iloc[i][0]) / (np.abs(self.pfit.iloc[i][0]) + 0.0001))

                normalRandom = np.random.normal(
                    0, tempSigma, self.dim)                     # 产生dim个正太分布随机数

                for j in np.arange(self.dim):                   # 更新公鸡位置
                    self.x.iloc[i][j] = self.px.iloc[i][j] * \
                        (1 + normalRandom[j])
                    if(self.x.iloc[i][j] > self.upb):
                        self.x.iloc[i][j] = self.upb
                    elif(self.x.iloc[i][j] < self.lowb):
                        self.x.iloc[i][j] = self.lowb
            # print(mate)
            # print("公鸡更新后的位置：")
            # print(self.x)

            for i in np.arange(self.rNum, self.rNum + self.hNum):

                while (True):  # 随机产生另外公鸡或母鸡的标签
                    anotherHens = np.random.randint(0, i)
                    if(anotherHens != mate[i - self.rNum]):
                        break

                c1 = np.exp((self.pfit.iloc[i][0] - self.pfit.iloc[int(mate[i - self.rNum])][0]
                             ) / (np.abs(self.pfit.iloc[i][0]) + 0.000000001))  # 更新c1 c2
                c2 = np.exp(self.pfit.iloc[anotherHens][0] -
                            self.pfit.iloc[i][0])

                for j in np.arange(self.dim):  # 更新母鸡位置

                    self.x.iloc[i][j] = self.px.iloc[i][j] + c1 * np.random.rand() * \
                        (self.px.iloc[int(mate[i - self.rNum])][j] - self.px.iloc[i][j]) + \
                        c2 * np.random.rand() * \
                        (self.px.iloc[anotherHens][j] - self.px.iloc[i][j])
                    if(self.x.iloc[i][j] > self.upb):
                        self.x.iloc[i][j] = self.upb
                    elif(self.x.iloc[i][j] < self.lowb):
                        self.x.iloc[i][j] = self.lowb
            # print("母鸡跟新后的位置：")
            # print(self.x)

            for i in np.arange(self.rNum + self.hNum, self.pop):
                for j in np.arange(self.dim):                        # 更新小鸡位置
                    self.x.iloc[i][j] = self.px.iloc[i][j] + 2 * np.random.rand() *\
                        (self.px.iloc[int(
                            mother[i - self.rNum - self.hNum])][j] - self.px.iloc[i][j])
                    if(self.x.iloc[i][j] > self.upb):
                        self.x.iloc[i][j] = self.upb
                    elif(self.x.iloc[i][j] < self.lowb):
                        self.x.iloc[i][j] = self.lowb
            # print("小鸡跟新后的位置：")
            # print(self.x)
            for i in np.arange(self.pop):  # 跟新鸡的适应度
                xi = self.x.iloc[i]
                self.fit[i] = self.test.Fitness(xi)

            self.pfit = pd.DataFrame(self.fit)
            self.gfit = self.pfit.min()   # 更新全局最优适应度
            self.ind = self.pfit.idxmin()
            self.gbest = self.x.iloc[self.ind]  # 更新全局最优位置
            self.gfit_list = np.append(self.gfit_list, self.gfit[0])
            # print(self.gbest)
            # print(self.gfit[0])
        # print(self.gfit_list)
        fig = plt.figure(dpi=128, figsize=(10, 6))
        plt.plot(np.arange(self.m), self.gfit_list, c='red')
        plt.title('50 iterations of fitness change', fontsize=24)
        plt.xlabel('Number of iterations', fontsize=16)
        plt.ylabel('Fitness', fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize='16')
        plt.show()
        # plt.savefig('Sphere_plot.svg')
