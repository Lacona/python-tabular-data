#! /usr/bin/env python3
# import pdb; pdb.set_trace()
import sys

def iris_scatter(filename):
# import packages 
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy import stats

# import dataset
    filename = pd.read_csv(sys.argv[1])
   
# create the scatterplots with regression line    
# Explanation of the commands: hue = from which variable the groups are defined, x and y define the variables for the x and y axis, ci = this option adds a confidence interval, height changes the size of the output, x/ylabel = label x/y axis,title = adds a titel, show = the output is shown but not saved, savefig = figure is saved  
    sns.set_style("whitegrid")
    sns.lmplot(data=filename, hue="species", x="petal_length_cm", y="sepal_length_cm", ci=None, height=6)
    plt.xlabel("Pengulin")
    plt.ylabel("Dodo")
    plt.xlim(0,8)
    plt.title("Scatterplots with regression line")
    
# show and save the output
    plt.show()
    plt.savefig("scatterplots.png")

if __name__ == '__main__':
    iris_scatter(sys.argv[1])

