import matplotlib.pyplot as plt
from die import Die

die_1 = Die()
die_2 = Die()

results = [die_1.roll() + die_2.roll() for roll_num in range(50000)]

max_result = die_1.num_sides + die_2.num_sides

frequencies = [results.count(frequency)
               for frequency in range(2, max_result + 1)]

x_labels = [num for num in range(2, max_result + 1)]

plt.scatter(x_labels, frequencies, s=5)

plt.show()
