class Movie:
    def __init__(self, title, year, rating, genres):
        self.title = title
        self.year = year
        self.rating = rating
        self.genres = genres

    def __str__(self):
        genres_str = ",".join(self.genres)
        return f"\nMovie: {self.title}({self.year}) \nRating: {self.rating} \nGenres: {genres_str}\n"
    
    def __repr__(self):
        return f"Movie(title={self.title}, year={self.year}, rating={self.rating}, genres={self.genres})"
    
    def is_classic(self):
        return self.year < 2000
    
    def is_hit(self):
        return self.rating > 8.0
    
    def add_genre(self, genre):
        if genre not in self.genres:
            self.genres.append(genre)

m = Movie("The Matrix", 1999, 8.7, ["Sci-Fi"])
print(m.is_classic())  # True
print(m.is_hit())      # True
m.add_genre("Action")
print(m)
