import matplotlib.pyplot as plt
x_values = list(range(1, 1001))
y_values = list(x**2 for x in x_values)
plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues, edgecolor='none', s=5)

# 设置图表标题并给坐标周加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])
plt.savefig('scatterTest.png', bbox_inches='tight')
