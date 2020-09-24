#!usr/bin/python3

import pandas as pd

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def main():
    excel_file = 'movies.xls'

    movies = pd.read_excel(excel_file)

    sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
    sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)

    all_movies = pd.concat([sheet1, sheet2, sheet3])

    print(all_movies.shape)

    sorted_by_rating = all_movies.sort_values(["IMDB Score"], ascending=False)

    print(sorted_by_rating.head(30))

     # create a stacked bar graph
    sorted_by_rating['IMDB Score'].head(30).plot(kind="barh")
    # save the figure as stackedbar.png
    plt.tight_layout()
    plt.savefig("/home/student/static/stackedbar.png")

if __name__ == "__main__":
    main()
