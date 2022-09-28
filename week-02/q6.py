from pandas import read_excel
from urllib.request import urlretrieve

xlsxFileName, _ = urlretrieve(
    'https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.xlsx')
gapminder = read_excel(xlsxFileName)

# print(gapminder)
print(gapminder[gapminder['year'] == 2002][['pop']].sum())
print(gapminder[gapminder['year'] == 2002][['lifeExp', 'gdpPercap']].mean())
