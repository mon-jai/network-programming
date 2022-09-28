from pandas import read_csv

data = read_csv("president_heights.csv")

print(data.describe())
print(data.sort_values(by=['height(cm)'], ascending=False).head(5))
print(data[data['height(cm)'] > 180].sort_values(by=['height(cm)']).head(5)) # https://stackoverflow.com/a/46165056
