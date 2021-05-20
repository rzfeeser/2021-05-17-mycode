import pandas

# this 10 of the highest grossing movies
df = pandas.read_excel("top10movies.xlsx")

# just write out the top 2 grossing movies to excel
df.head(2).to_json("top2movies.json")

