import pandas

# this 10 of the highest grossing movies
df = pandas.read_json("top10movies.json")

# just write out the top 10 grossing movies to excel
df.head(5).to_excel("top5movies.xlsx")

