# Visualization with Seaborn and Matplotlib
# Use the “Titanic” dataset from Seaborn and do the following:

import seaborn as sns
import matplotlib.pyplot as plt

# Countplot: Passenger Count by Embarked Port
# ● Create a countplot to display the number of passengers who boarded from each port (embarked), separated by sex.

df=sns.load_dataset("titanic")
print(df.columns)

# sns.countplot(data=df, x="embark_town", hue="sex")
# plt.show()

# insight : countplot used to represent the count of each features by a bar graph. here emarked is the feature ane it has 3 location

# Swarmplot: Age Distribution across Classes
# ● Create a swarmplot to visualize the distribution of age across passenger classes (pclass), categorized by sex.

# sns.swarmplot(x="sex",y="class",data=df)
# plt.show()

# insight : Swarm plot is used to represent count of a feature amoung a category and it looks like warm points are arranged ad continuos dots


# Pie Chart: Gender Distribution
# ● Create a pie chart using Matplotlib to show the percentage of male vs. female passengers.
# - Add percentage labels using autopct - Use explode for one slice to highlight it.

# gender_counts = df["sex"].value_counts()
# print(gender_counts)
# plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', explode=[0.05, 0])
# plt.show()


# insight : Here pie chart is used to represent the percentage representation of parameters, here the gender is the parameter taken and we can give percentage



# Heatmap: Correlation Matrix
# ● Create a heatmap to show correlations between age, fare, pclass, sibsp, parch, and survived. (Use seaborn.heatmap with annotations)

# df_selected=df.select_dtypes(include="number")
# sns.heatmap(df_selected.corr(), annot=True)
# plt.show()


# insight : corelation matrix is used to represent the relationship among the numerical features. here the correlation of features are shown with valus and colour
            #same parameter meets 1 value and its diagonal


# Violin Plot: Fare by Class and Gender
# ● Create a violin plot to visualize fare distribution across classes, separated by gender.

# sns.violinplot(x="fare", y="class", data=df, hue="sex")
# plt.show()



# insight : It looks like a violin. here a box plot can be sean in side violin



# Scatter Plot: Age vs Fare
# ● Create a scatter plot to explore the relationship between age and fare, colored by survival status.
# ● Use a seaborn scatterplot with hue='survived'. Each plot must have titles, labels, and legends where needed.

sns.scatterplot(x="age", y="fare", data=df, hue="survived", legend=True)
plt.title("Age vs Fare")
plt.show()


# insight : It is like the data points are scattered in plot, two parameters are used to plot

# Write short observations under each plot explaining insights.