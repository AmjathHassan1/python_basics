import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data=sns.load_dataset('titanic')
print(data.head(3))

# Count plot : Shows the frequency  of occurence of each category in a categorial variable.
# Seaboaarn's countplot() function is usefull for visualizing the distribution of categorial data

# sns.countplot(x='class', data=data, palette='Set1')
# plt.title('Count plot of passengers Class')
# plt.show()

# Bar Plot

# sns.barplot(x='sex',y='fare',data=data, palette='Set1')
# plt.title('Average fare by gender')
# plt.show()


# Scatter Plot

# sns.scatterplot(x='age', y='fare', data=data, hue='sex', palette='coolwarm')
# plt.title('Scatter Plot of Age vs Fare ')
# plt.show()

# Line Plot

# sns.lineplot(x='age', y='fare', data=data, hue='sex')
# plt.title('Line Plot of Age vs Fare ')
# plt.show()

# Box Plot
#
# sns.boxplot(x='class', y='age', data=data, palette='Set1')
# plt.title('Box Plot of Age by class ')
# plt.show()


# Histogram Plot

# sns.histplot(data['age'],bins=30, kde=True, color='purple')
# plt.title('Histogram of age ')
# plt.show()


# Density Plot: Used to visualize the distribution of data

# sns.kdeplot(data.age, shade=True, color='green')  # kernel density estimation
# plt.title('Density plot of age')
# plt.show()


# Violin Plot: A Violin plot combines the features of a box plot and a kernal density estimation
# plot to visualize the distribution of a numerical variable across different across different categories

# sns.violinplot(x='class',y='age',data=data, palette='muted')
# plt.title('Violin Plot of Age by Class')
# plt.show()
#


# Strip Plot: A Strip Plot is a one-Dimensional scater plot where the category variables is plotted on the x-axis
# and the continuous variable is plotted on the y-axis Each data point is represented as a single point along the
# categorical axis . Seaboarn's stripplot() function is used to create strip plots

# sns.stripplot(x='class', y='age', data=data)
# plt.title('Swarm plot of Age by class')
# plt.show()


# Swarm Plot : A plot is similar to a strip plot , but it spreads out the points to avoid overlap , giving a
# better visualization of the distribution of the data . Seaboarn's warmplot() function is used to create  swarm plots

# sns.swarmplot(x='class', y='age', data=data)
# plt.title('Swarm plot age by class')
# plt.show()

# Heat Map: Used to visualize correlation between numerical variables

# data1=data.select_dtypes(include='number')
# cor=data1.corr()
# sns.heatmap(cor,annot=True,cmap='coolwarm')
# plt.title('Correlation Heatmap')
# plt.show()


# Pair Plot : A pair plot creates a grid of scatter plots for all pairs of varriables in a dataset , along with
# histograms for each variables's distribution

sns.pairplot(data, hue='sex', palette='husl', height=3, aspect=1.2)
plt.suptitle('Pair Plot of titaanic data ', y=1.02)
plt.show()



































