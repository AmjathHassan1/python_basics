# Matplotlib questions
#
import matplotlib.pyplot as plt
import numpy as np
# 1.Display the number of students in each department:
#
departments = ['CSE', 'ECE', 'ME', 'CE', 'EEE']
students = [120, 100, 80, 75, 90]
#
#  Add labels, color bars differently, and rotate x-axis labels.
#

# plt.bar(departments, students)
# plt.xlabel('Department')
# plt.ylabel('Students')
# plt.xticks(rotation=45)
#
# plt.show()

#
# 2.Plot the same data above but as a horizontal bar chart.

# plt.barh(departments, students)
# plt.ylabel('Department')
# plt.xlabel('Students')
# plt.show()

# 3.Plot a histogram showing the distribution of students’ marks (generate random data using NumPy).

marks = np.random.randint(0, 101, 100)
print(marks)
plt.hist(marks, color='skyblue')

plt.show()


# 4.Create a pie chart for market share of mobile companies:

# companies = ['Samsung', 'Apple', 'Xiaomi', 'OnePlus', 'Others']
# share = [35, 25, 20, 10, 10]
# #
# plt.pie(share, labels=companies, colors=['red', 'green', 'blue', 'yellow'])
# plt.legend(loc='upper right')
# plt.show()

#  Add labels, percentages, and explode one slice.

# companies = ['Samsung', 'Apple', 'Xiaomi', 'OnePlus', 'Others']
# share = [35, 25, 20, 10, 10]
# # #
# explode = [0.1, 0, 0, 0, 0]
# plt.pie(share, labels=companies, colors=['red', 'green', 'blue', 'yellow', 'violet'], autopct='%1.1f%%', explode=explode, shadow=True  )
# plt.axis('equal')
# plt.show()
# plt.legend(loc='upper right')
# plt.show()

# 5.Create a figure with 4 subplots (2x2 grid):
#
# Line plot
#
# Bar graph
#
# Scatter plot
#
# Pie chart


# x=[1,2,3,4,5,6,7]
# y=[23,12,10,40,52,30,15]
#
# plt.subplot(2,2,1)
# plt.plot(x,y)
#
# plt.subplot(2,2,2)
# plt.bar(x,y)
#
# plt.subplot(2,2,3)
# plt.scatter(x,y)
# #
# plt.subplot(2,2,4)
# plt.pie(y, labels=['A', 'B', 'C', 'D', 'E','F','G'])
# plt.show()