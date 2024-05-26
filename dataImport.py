class Movie:
    def __init__(self, id, shortName, longName):
        self.id = id
        self.shortName = shortName
        self.longName = longName

    def __repr__(self):
        return f"Movie(id={self.id}, shortName='{self.shortName}', longName='{self.longName}')"


def importData(filename, start, end):
    movies = []
    try:
        with open(filename, 'r', encoding='latin-1') as file:
            for current_line_number, line in enumerate(file, start=1):
                if start <= current_line_number <= end:
                    parts = line.strip().split('\t') 
                    if len(parts) == 3:
                        id = int(parts[0])
                        shortName = parts[1].strip()
                        longName = parts[2].strip()
                        movie = Movie(id, shortName, longName)
                        movies.append(movie)
                    else:
                        print(f"Skipping malformed line: {line.strip()}")
                elif current_line_number > end:
                    break
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return movies

