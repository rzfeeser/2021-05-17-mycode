#!/usr/bin/python3

import pandas as pd

# these following two lines are for writing to file
# use this when you are not rendering to a window
import matplotlib
matplotlib.use('Agg')

# create some graphs
import matplotlib.pyplot as plt

def main():
    # define the name of our xls file
    excel_file = 'movies.xls'

    # create a DataFrame (DF) object. EASY!
    # because we did not specify a sheet
    # only the first sheet was read into the DF
    movies = pd.read_excel(excel_file)

    # show the first five rows of our DF
    # DF has 5 rows and 25 columns (indexed by integer)
    print(movies.shape)
    input()
    print(movies.head())
    input()
    print(movies.head(7))
    input()
    print(movies.head(22))

    # Choose the first column "Title" as
    # index (index=0)
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    # DF has 5 rows and 24 columns (indexed by title)
    print(movies_sheet1.head())

    # grab the next 2 sheets as well
    movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
    # DF has 5 rows and 24 columns (indexed by title)
    print(movies_sheet2.head())

    movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
    # DF has 5 rows and 24 columns (indexed by title)
    print(movies_sheet3.head())

    # combine all DFs into a single DF called movies
    movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])

    # number of rows and columns (5042, 24)
    print(movies.shape)
    input()

    # unfortunately our data has some duplicates in it
    # we can remove them quickly with the .drop_duplicates() method
    # this returns a dataframe, or None if .drop_duplicates(inplace=True)
    movies.drop_duplicates(inplace=True)
    
    # take a peek at how our dataframe changed after removing duplicates
    print(movies.shape)
    input()
    # sort DataFrame based on Gross Earnings
    sorted_by_gross = movies.sort_values(["Gross Earnings"], ascending=False)

    # Data is sorted by values in a column
    # display the top 10 movies by Gross Earnings.
    # passing the 10 values to head returns the top 10 not the default 5
    print(sorted_by_gross.head(10))

    # create a stacked bar graph
    sorted_by_gross['Gross Earnings'].head(10).plot(kind="barh")
    # save the figure as stackedbar.png
    plt.savefig("/home/student/static/stackedbar.png", bbox_inches='tight')

    print(dir(movies))

    sorted_by_gross.head(10).to_json("top10movies.json")
    sorted_by_gross.head(10).to_excel("top10movies.xlsx")
    sorted_by_gross.head(10).to_csv("top10movies.csv")

if __name__ == "__main__":
    main()
