
# movie recs I liked (also some animes)
import random

# Movie database with genres and ratings (also some shows)
movies = {
    "action": {"Mad Max": 0, "Attack on Titan": 0, "John Wick": 0},
    "comedy": {"Sakamoto Days": 0, "Superbad": 0, "Step Brothers": 0},
    "drama": {"Shawshank Redemption": 0, "Forrest Gump": 0, "Apothecary Diaries": 0},
    "sci-fi": {"Interstellar": 0, "Inception": 0, "Jujustsu Kaisen": 0}
}

def recommend_movie(genre):
    if genre in movies:
        movie_list = list(movies[genre].keys())
        recommendation = random.choice(movie_list)
        print(f"🎬 I recommend you watch: {recommendation}")
        return recommendation
    else:
        print("Sorry, we don't have that genre yet.")
        return None

def rate_movie(genre, movie):
    try:
        rating = int(input(f"Rate {movie} from 1-5: "))
        if 1 <= rating <= 5:
            movies[genre][movie] = rating
            print(f"Thanks! You rated {movie} {rating}/5")
        else:
            print("Invalid rating. Please enter 1-5.")
    except:
        print("Invalid input. Rating must be a number.")

def main():
    print("🎥 Welcome to the Movie Recommendation System!")
    while True:
        genre = input("Enter a genre (action/comedy/drama/sci-fi) or 'quit' to exit: ").lower()
        if genre == "quit":
            break
        movie = recommend_movie(genre)
        if movie:
            rate_movie(genre, movie)
        print("\nCurrent ratings:")
        for g, m in movies.items():
            print(f"{g.title()}: {m}")
        print("-" * 30)

if __name__ == "__main__":
    main()
