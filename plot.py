#! /usr/bin/env python3
#import pdb; pdb.set_trace()
import sys

# define x and y and filename
x = str(sys.argv[2])
y = str(sys.argv[3])   

def iris_scatter(filename, x, y):
# import packages 

# import dataset
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy import stats
    filename = pd.read_csv(sys.argv[1])
# create the scatterplots with regression line    
# Explanation of the commands: hue = from which variable the groups are defined, x and y define the variables for the x and y axis, ci = this option adds a confidence interval, height changes the size of the output, x/ylabel = label x/y axis,title = adds a titel, show = the output is shown but not saved, savefig = figure is saved  
    sns.set_style("whitegrid")
    sns.lmplot(data=filename, hue="species", x="x", y="y", ci=None, height=6)
    plt.xlabel("Pengulin")
    plt.ylabel("Dodo")
    plt.xlim(0,8)
    plt.title("Scatterplots with regression line")
    
# show and save the output
    plt.show()
    plt.savefig("scatterplots.png")

if __name__ == '__main__':
    import pandas as pd
    filename = pd.read_csv(sys.argv[1])
    iris_scatter(filename, x, y)

