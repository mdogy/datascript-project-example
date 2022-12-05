
import numpy as np
import requests as rq
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    """This function runs the program getting the data from the data url 
    and plotting the pairs and giving a report"""
    # What is the data of the url?
    url = "https://bit.ly/palmerpenguinscsv"
    df = pd.read_csv(url)
    # Select the columns to plot
    df = df[["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g","species"]]
    # Single out the species for color(hue)
    pp = sns.pairplot(data=df,hue="species")
    # Save the plot to a file
    pp.savefig("pairplot.png")
    # Make a report and save to a file    
    with open("report.txt", "w") as f:
        f.write("# Data Summary\n\n")
        f.write("## df.info()\n\n")
        df.info(buf=f)
        f.write("\n\n## df.describe()\n\n")
        f.write(str(df.describe()))


if __name__ == "__main__":
    main()
