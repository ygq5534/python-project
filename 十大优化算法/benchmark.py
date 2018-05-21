import numpy as np
import pandas as pd
'''十大标准测试函数'''

class Benchmark:
    def __init__(self,dim):
        self.xi = np.zeros(dim)
        self.fit = np.zeros(10)
    
    def Fitness(self,xi):
        self.xi = xi
        funcs = (Sphere,Schwefel1,Schwefel2,Schwefel3,Rosenbrock,Quartric,GeneralizedSchwefek,
            Rastrigin,Ackley,Griewank)
        for i in np.arange(10):
            self.fit[i] = funcs[i]()
        return self.fit

        

    def Sphere(self):
        result = 0
        for xij in self.xi:
            result += xij*xij
        return result
    
    def Schwefel1(self):
        result = 0
        temp = 0
        for xij in self.xi:
            result += np.abs(xij)
            temp *= np.abs(xij)
        return result+temp
    
    def Schwefel2(self):
        result = 0
        for i in np.arange(self.xi.size):
            temp = 0
            for j in np.arange(i):
                temp += xi[j]*xi[j]
            result += temp
        return result
    
    def Schwefel3(self):
        max = self.xi.abs().max()
        return max
    
    def Rosenbrock(self):
        result = 0
        temp1 = 0
        temp2 = 0
        for i in np.arange(self.xi.size-1):
            temp1 = 100 * (self.xi[i+1]-self.xi[i]*self.xi[i]) * (self.xi[i+1]-self.xi[i]*self.xi[i])
            temp2 = (self.xi[i]-1) * (self.xi[i]-1)
            result = temp1 + temp2
        return result
    
    def Quartric(self):
        result = 0
        for i in np.arange(self.xi.size):
            result += (i+1) * np.math.pow(self.xi[i],4) + np.random.rand()
        return result
    
    def GeneralizedSchwefek(self):
        result = 0
        for i in np.arange(self.xi.size):
            result += -self.xi[i] * np.math.sin(np.math.sqrt(self.xi[i]))
        return result
    
    def Rastrigin(self):
        result = 0
        for i in np.arange(self.xi.size):
            result += self.xi[i] * self.xi[i] - 10 * np.math.cos(2 * np.pi * self.xi[i])
        return result + 10 *  self.xi.size
    
    def Ackley(self):
        result = 0
        temp1 = 0
        temp2 = 0
        temp3 = 0
        temp4 = 0
        for i in np.arange(self.xi.size):
            temp1 += self.xi[i] * self.xi[i]
            temp2 += np.math.cos(2*np.pi*self.xi[i])
        temp3 = -20 * np.exp(-0.2*np.math.sqrt((1/self.xi.size)*temp1)
        temp4 = -1 * np.exp(temp2/self.xi.size)
        result = temp3 + temp4 + 20 +np.exp(1)
        return result
    
    def Griewank(self):
        result = 0
        temp1 = 0
        temp2 = 0
        for i in np.arange(self.xi.size):
            temp1 += self.xi[i]*self.xi[i]
            temp2 *= np.math.cos(self.xi[i]/np.math.sqrt(i))
        result = temp1/4000 - temp2 + 1
    
    

        



        