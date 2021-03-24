#! /usr/bin/env python3

if __name__ == '__main__':

# import packages 
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy import stats

# import dataset
    iris = pd.read_csv("iris.csv")

# create the scatterplots with regression line    
# Explanation of the commands: hue = from which variable the groups are defined, x and y define the variables for the x and y axis, ci = this option adds a confidence interval, height changes the size of the output, x/ylabel = label x/y axis,title = adds a titel, show = the output is shown but not saved, savefig = figure is saved  
    sns.set_style("whitegrid")
    sns.lmplot(data=iris, hue="species", x="petal_length_cm", y="sepal_length_cm", ci=None, height=6)
    plt.xlabel("Pengulin")
    plt.ylabel("Dodo")
    plt.xlim(0,8)
    plt.title("Scatterplots with regression line")

# show and save the output
    plt.show()
    plt.savefig("scatterplots_iris.png")

# subsetting into different dataframes:
#def subset(dataframe, list_of_species):
#    grouped = dataframe.query('species in @list_of_species').groupby("species")
#    return [grouped.get_group(d) for d in list_of_species]
#versicolor = dataframe[dataframe.species == "Iris_versicolor"]
#virginica = (dataframe.species, ["Iris_virginica"])
#setosa = (dataframe.species, ["Iris_setosa"])
#print(subsets)

#x = versicolor.petal_length_cm
#y = versicolor.sepal_length_cm
#regression = stats.linregress(x, y)
#slope = regression.slope
#intercept = regression.intercept
#plt.scatter(x, y, label = '3 scatter plots')
#plt.plot(x, slope * x + intercept, label = 'Fitted line')
#plt.xlabel("Petal lenght in cm")
#plt.ylabel("Sepal length in cm")
#plt.legend()
#plt.savefig("3-scatter.png")

