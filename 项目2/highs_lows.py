import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取日期，最高气温和最低气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, dates, lows = [], [], []
    for row in reader:
        try:
            high = int(row[1])
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing date')
        else:
            highs.append(high)
            dates.append(current_date)
            low = int(row[3])
            lows.append(low)

# 根据数据绘制图形

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, linewidth='1', c='red', alpha=0.5)
plt.plot(dates, lows, linewidth='1', c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("Daily high and low temperatures, 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize='16')

plt.show()
