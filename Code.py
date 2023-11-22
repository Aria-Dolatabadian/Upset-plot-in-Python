import pandas as pd
from upsetplot import from_memberships
from upsetplot import UpSet

movies = pd.read_csv("data.csv")
movies_by_genre = from_memberships(movies.Genre.str.split(','), data=movies)
print(movies_by_genre)


UpSet(movies_by_genre, min_subset_size=15, show_counts=True).plot()
from matplotlib import pyplot
pyplot.show()
