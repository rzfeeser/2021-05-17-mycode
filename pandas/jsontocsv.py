import pandas

# this 10 of the highest grossing movies
df = pandas.read_json("top10movies.json")

# just write out the top 7 grossing movies to csv format
df.head(7).to_csv("top7movies.csv")

