from nester.nester import print_lol
import nester.nester
movies = ["The holy", 1975, "Terry Jones", 91,
          ["Graham Champman", ["Michael palin", "John Cleese",
           'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]
# 'The life','the meaning'
# for movie in movies:
#     if isinstance(movie, list):
#         for each_movie in movie:
#             if isinstance(each_movie,list):
#                 for deep_movie in each_movie:
#                     print(deep_movie)
#             else:
#                 print(each_movie)
#     else:
#         print(movie)
# print(movies)
print_lol(movies)

