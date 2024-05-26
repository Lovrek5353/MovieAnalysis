import dataImport 

def main():

    filename = 'movie.txt'
    print("First set: ")
    movies1 = dataImport.importData(filename, 23163, 38162)
    """
    for movie in movies1:
        print(movie)
    """

    print("\nSecond set: ")
    movies2 = dataImport.importData(filename, 541033, 556032)

    """
    for movie in movies2:
        print(movie)
    """
    # Combine movie lists
    all_movies = movies1 + movies2

    print("\nAll movies:")
    """
    for movie in all_movies:
        print(movie)
    """        

if __name__ == "__main__":
    main()
