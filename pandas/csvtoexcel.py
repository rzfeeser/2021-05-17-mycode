import pandas

# this 10 of the highest grossing movies
df = pandas.read_csv("top10movies.csv")

# just write out the top 5 grossing movies to excel
df.head(5).to_excel("top5movies.xlsx")

