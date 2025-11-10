from faker import Faker
import random
import uuid
import json
from datetime import datetime

fake = Faker()

def generate_mock_movies(n=25):
    movies = []
    
    categories = [
        "Action", "Adventure", "Comedy", "Drama", "Sci-Fi", "Horror",
        "Thriller", "Romance", "Animation", "Fantasy", "Documentary"
    ]
    
    producers = [
        "Christopher Nolan", "Steven Spielberg", "Quentin Tarantino", 
        "Martin Scorsese", "Greta Gerwig", "James Cameron", 
        "Patty Jenkins", "Denis Villeneuve", "Jordan Peele", "Ridley Scott"
    ]
    
    for _ in range(n):
        category = random.choice(categories)
        producer = random.choice(producers)
        
        movie = {
            "id": str(uuid.uuid4()),
            "title": fake.catch_phrase(),
            "category": category,
            "description": fake.sentence(nb_words=15),
            "poster_url": fake.image_url(width=400, height=600),
            "trailer_url": f"https://youtube.com/watch?v={fake.lexify(text='???????????')}",
            "duration": random.randint(80, 180),
            "release_year": random.randint(1990, 2025),
            "rating": round(random.uniform(1.0, 10.0), 1),
            "cast": ", ".join(fake.name() for _ in range(random.randint(2, 5))),
            "producer": producer,
            "is_featured": fake.boolean(chance_of_getting_true=30),
            "views": random.randint(1000, 100000),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "is_liked": fake.boolean(),
        }
        
        movies.append(movie)
    
    return movies


if __name__ == "__main__":
    mock_movies = generate_mock_movies(20)
    
    # Write to JSON file
    output_file = "mock_movies.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(mock_movies, f, indent=2, ensure_ascii=False, default=str)
    
    print(f"✅ Generated {len(mock_movies)} mock movies.")
    print(f"📁 Written to {output_file}")
