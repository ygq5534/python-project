import numpy as np
import pandas as pd
'''十大标准测试函数'''


class Benchmark:
    def __init__(self, dim):
        self.xi = np.zeros(dim)
        # self.xi = xi
        self.fit = np.zeros(10)

    def Sphere(self):
        result = 0
        for xij in self.xi:
            result += xij * xij
        return result

    def Schwefel1(self):
        result = 0
        temp = 0
        for xij in self.xi:
            result += np.abs(xij)
            temp *= np.abs(xij)
        return result + temp

    def Schwefel2(self):
        result = 0
        for i in np.arange(self.xi.size):
            temp = 0
            for j in np.arange(i):
                temp += self.xi[j] * self.xi[j]
            result += temp
        return result

    def Schwefel3(self):
        max = np.abs(self.xi).max()
        return max

    def Rosenbrock(self):
        result = 0
        temp1 = 0
        temp2 = 0
        for i in np.arange(self.xi.size - 1):
            temp1 = 100 * (self.xi[i + 1] - self.xi[i] * self.xi[i]) * \
                (self.xi[i + 1] - self.xi[i] * self.xi[i])
            temp2 = (self.xi[i] - 1) * (self.xi[i] - 1)
            result = temp1 + temp2
        return result

    def Quartric(self):
        result = 0
        for i in np.arange(self.xi.size):
            result += (i + 1) * np.math.pow(self.xi[i], 4) + np.random.rand()
        return result

    def GeneralizedSchwefek(self):
        result = 0
        for i in np.arange(self.xi.size):
            result += self.xi[i] * \
                np.math.sin(np.math.sqrt(np.abs(self.xi[i])))
        return -1 * result

    def Rastrigin(self):
        result = 0
        for i in np.arange(self.xi.size):
            result += self.xi[i] * self.xi[i] - 10 * \
                np.math.cos(2 * np.pi * self.xi[i])
        return result + 10 * self.xi.size

    def Ackley(self):
        result = 0
        temp1 = 0
        temp2 = 0
        temp3 = 0
        temp5 = 0
        for i in np.arange(self.xi.size):
            temp1 += self.xi[i] * self.xi[i]
            temp2 += np.math.cos(2 * np.pi * self.xi[i])
        temp3 = -20 * np.exp(-0.2 * np.math.sqrt((1 / self.xi.size) * temp1))
        temp4 = -1 * np.exp(temp2 / self.xi.size)
        result = temp3 + temp4 + 20 + np.exp(1)
        return result

    def Griewank(self):
        result = 0
        temp1 = 0
        temp2 = 0
        for i in np.arange(self.xi.size):
            temp1 += self.xi[i] * self.xi[i]
            temp2 *= np.math.cos(self.xi[i] / np.math.sqrt(i + 1))
        result = (temp1 / 4000) - temp2 + 1
        return result

    def Fitness(self, xi):
        self.xi = xi
        funcs = (self.Sphere, self.Schwefel1, self.Schwefel2, self.Schwefel3, self.Rosenbrock, self.Quartric, self.GeneralizedSchwefek,
                 self.Rastrigin, self.Ackley, self.Griewank)
        for i in np.arange(10):
            self.fit[i] = funcs[i]()

        # self.fit[0] = self.Sphere()
        # self.fit[1] = self.Schwefel1()
        # self.fit[2] = self.Schwefel2()
        # self.fit[3] = self.Schwefel3()
        # self.fit[4] = self.Rosenbrock()
        # self.fit[5] = self.Quartric()
        # self.fit[6] = self.GeneralizedSchwefek()
        # self.fit[7] = self.Rastrigin()
        # self.fit[8] = self.Ackley()
        # self.fit[9] = self.Griewank()
        # print(self.fit[9])
        return self.fit
