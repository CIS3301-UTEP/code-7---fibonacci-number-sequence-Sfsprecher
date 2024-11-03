filename = "my_first_file.txt"

file = open(filename,mode="w")

movies = ["Scream","IT","The Nun","Anabelle","Jason"]

for movies in movies:
    # print(movie)
    file.write(movies)
    file.write('\n')
