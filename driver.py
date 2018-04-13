# Importing modules
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# # Reading in datasets/book1.csv
# book1 = pd.read_csv('./asoiaf/data/asoiaf-book1-edges.csv')
#
# # Printing out the head of the dataset
# # print(book1.head())
#
# # Creating an empty graph object
# G_book1 = nx.Graph()
#
#
# # Iterating through the DataFrame to add edges
# for index, row in book1.iterrows():
#     G_book1.add_edge(row['Source'], row['Target'], weight=row['weight'])
#
# # nx.draw(G_book1)
# # plt.show()

# Creating a list of networks for all the books
books = []
book_fnames = ['./asoiaf/data/asoiaf-book1-edges.csv', './asoiaf/data/asoiaf-book2-edges.csv', './asoiaf/data/asoiaf-book3-edges.csv', './asoiaf/data/asoiaf-book4-edges.csv', './asoiaf/data/asoiaf-book5-edges.csv']
for book_fname in book_fnames:
    book = pd.read_csv(book_fname)
    G_book = nx.Graph()
    for _, edge in book.iterrows():
        G_book.add_edge(edge['Source'], edge['Target'], weight=edge['weight'])
    books.append(G_book)


# Calculating the degree centrality of book 1
deg_cen_book1 = nx.degree_centrality(books[0])

# Calculating the degree centrality of book 5
deg_cen_book5 = nx.degree_centrality(books[4])

# Sorting the dictionaries according to their degree centrality and storing the top 10
sorted_deg_cen_book1 = sorted(deg_cen_book1.items(), key=lambda x: x[1], reverse=True)

# Sorting the dictionaries according to their degree centrality and storing the top 10
sorted_deg_cen_book5 = sorted(deg_cen_book5.items(), key=lambda x: x[1], reverse=True)

# Printing out the top 10 of book1 and book5
print('Book 1:')
for i in range(10):
    print(str(i) + ': ' + str(sorted_deg_cen_book1[i]))
print('Book 5:')
for i in range(10):
    print(str(i) + ': ' + str(sorted_deg_cen_book5[i]))

# Creating a list of degree centrality of all the books
evol = [nx.degree_centrality(book) for book in books]

# Creating a DataFrame from the list of degree centralities in all the books
degree_evol_df = pd.DataFrame.from_records(evol).fillna(0)
# print(degree_evol_df.head())
# print(degree_evol_df.describe())

# Plotting the degree centrality evolution of a few central characters
# degree_evol_df['Eddard-Stark'].plot(legend=True)
# degree_evol_df['Tyrion-Lannister'].plot(legend=True)
# degree_evol_df['Jon-Snow'].plot(legend=True)
# degree_evol_df['Stannis-Baratheon'].plot(legend=True)
# degree_evol_df['Cersei-Lannister'].plot(legend=True)
# degree_evol_df['Jaime-Lannister'].plot(legend=True)
# degree_evol_df['Daenerys-Targaryen'].plot(legend=True)
#
# plt.show()

# Creating a list of betweenness centrality of all the books just like we did for degree centrality
evol = [nx.betweenness_centrality(book, weight='weight') for book in books]

# Making a DataFrame from the list
betweenness_evol_df = pd.DataFrame.from_records(evol).fillna(0)

# Finding the top 4 characters in every book
set_of_char = set()
for i in range(5):
    set_of_char |= set(list(betweenness_evol_df.T[i].sort_values(ascending=False)[0:4].index))
list_of_char = list(set_of_char)

# Plotting the evolution of the top characters
for char in list_of_char:
    print(char)
    betweenness_evol_df[char].plot(figsize=(13, 7), legend=True)

plt.show()
#
# # Creating a list of pagerank of all the characters in all the books
# evol = [nx.pagerank(book) for book in books]
#
# # Making a DataFrame from the list
# pagerank_evol_df = pd.DataFrame.from_records(evol)

# Finding the top 4 characters in every book
# set_of_char = set()
# for i in range(5):
#     set_of_char |= set(list(pagerank_evol_df.T[i].sort_values(ascending=False)[0:4].index))
# list_of_char = list(set_of_char)
#
# # Plotting the top characters
# for char in list_of_char:
#     pagerank_evol_df[char].plot(figsize=(13, 7), legend=True)

# plt.show()

# # Creating a list of pagerank, betweenness centrality, degree centrality
# # of all the characters in the fifth book.
# measures = [nx.pagerank(books[4]),
#             nx.betweenness_centrality(books[4], weight='weight'),
#             nx.degree_centrality(books[4])]
#
# # Creating the correlation DataFrame
# cor = pd.DataFrame.from_records(measures)
#
# # Calculating the correlation
# print(cor.T.corr())
#
# # Finding the most important character in the fifth book,
# # according to degree centrality, betweenness centrality and pagerank.
# p_rank, b_cent, d_cent = cor.idxmax(axis=1)
#
# # Printing out the top character according to the three measures
# print(p_rank)
# print(b_cent)
# print(d_cent)