import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

class RecommendationSystem:
    def __init__(self):
        print("Initializing Recommendation System...")
        # Movie dataset with features for content-based filtering
        data = {
            'movie_id': range(1, 21),
            'title': [
                'The Dark Knight', 'Inception', 'Interstellar', 'The Matrix', 'Avatar',
                'Titanic', 'The Avengers', 'Iron Man', 'Spider-Man: No Way Home', 'Batman Begins',
                'Shutter Island', 'The Prestige', 'Memento', 'The Departed', 'Gladiator',
                'John Wick', 'The Shawshank Redemption', 'Forrest Gump', 'The Godfather', 'Pulp Fiction'
            ],
            'genre': [
                'Action Crime Drama', 'Action Sci-Fi Thriller', 'Adventure Drama Sci-Fi',
                'Action Sci-Fi', 'Action Adventure Fantasy Sci-Fi', 'Drama Romance',
                'Action Adventure Sci-Fi', 'Action Adventure Sci-Fi', 'Action Adventure Sci-Fi',
                'Action Crime Drama', 'Mystery Thriller', 'Drama Mystery Sci-Fi',
                'Mystery Thriller', 'Crime Drama Thriller', 'Action Drama History',
                'Action Crime Thriller', 'Drama', 'Drama Romance', 'Crime Drama', 'Crime Drama'
            ],
            'description': [
                'Batman faces Joker chaos Gotham', 'Dream thief extracts secrets inception',
                'Astronauts travel wormhole save humanity', 'Hacker discovers world simulation',
                'Paraplegic marine alien world Pandora', 'Poor artist rich woman ship sinks',
                'Superheroes assemble fight Loki aliens', 'Genius billionaire builds weaponized suit',
                'Peter Parker multiverse villains return', 'Bruce Wayne trains becomes Batman',
                'US Marshal investigates psychiatric facility', 'Two stage magicians deadly rivalry',
                'Man short term memory hunts wife killer', 'Mole police mob Boston',
                'Betrayed Roman general gladiator revenge', 'Retired hitman seeks vengeance dog',
                'Two imprisoned men bond years', 'Man witnesses historical events',
                'Aging patriarch transfers control empire', 'Two hitmen boxer crime stories'
            ]
        }
        
        self.df = pd.DataFrame(data)
        self.df['features'] = self.df['genre'] + ' ' + self.df['description']
        
        # TF-IDF Vectorization
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.df['features'])
        
        # Cosine Similarity Matrix
        self.cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        print(f"System ready with {len(self.df)} items")
    
    def recommend(self, item_name, top_n=3):
        """Content-based filtering recommendation"""
        item_name = item_name.strip().lower()
        matches = self.df[self.df['title'].str.lower().str.contains(item_name)]
        
        if matches.empty:
            return None, f"'{item_name}' not found"
        
        idx = matches.index[0]
        original_name = self.df.loc[idx, 'title']
        
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
        
        indices = [i[0] for i in sim_scores]
        scores = [i[1] for i in sim_scores]
        
        recommendations = self.df.iloc[indices][['title', 'genre']].copy()
        recommendations['match_score'] = [round(s * 100, 1) for s in scores]
        
        return recommendations, original_name
    
    def show_items(self):
        print("\nAvailable Items:")
        for i, title in enumerate(self.df['title'], 1):
            print(f"{i:2}. {title}")

def main():
    print("=" * 60)
    print("CODSOFT TASK 4: RECOMMENDATION SYSTEM")
    print("Technique: Content-Based Filtering using TF-IDF")
    print("=" * 60)
    
    system = RecommendationSystem()
    system.show_items()
    
    while True:
        user_input = input("\nEnter item name | 'list' | 'exit': ").strip()
        
        if user_input.lower() == 'exit':
            print("Task 4 completed successfully!")
            break
        elif user_input.lower() == 'list':
            system.show_items()
        elif user_input:
            recs, name = system.recommend(user_input)
            if recs is None:
                print(f"Error: {name}")
            else:
                print(f"\nRecommendations for '{name}':")
                print("-" * 60)
                for _, row in recs.iterrows():
                    print(f"🎯 {row['title']} | {row['match_score']}% match")
                    print(f" Genre: {row['genre']}\n")

if __name__ == "__main__":
    main()