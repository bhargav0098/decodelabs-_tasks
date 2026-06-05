import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data(filepath):
    """Loads the job roles and skills dataset."""
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return None

def get_recommendations(user_input, df, top_n=3):
    """
    Core Recommendation Logic implementing TF-IDF and Cosine Similarity.
    """
    # UPGRADE: Combine the Role name and the Skills list into a single searchable string
    # This prevents the "0% match" issue if a user types a job title instead of a specific skill.
    df['Combined_Features'] = df['Role'] + " " + df['Skills']
    
    # Step 1: Ingestion - Combine user input with the new combined features
    all_data = [user_input] + df['Combined_Features'].tolist()
    
    # Step 2: Vector Mapping & Scoring using TF-IDF
    # This mathematically maps the text into numerical arrays
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(all_data)
    
    # The user profile is the first vector (index 0)
    user_vector = tfidf_matrix[0]
    # The item profiles are the rest of the vectors
    item_vectors = tfidf_matrix[1:]
    
    # Calculate Cosine Similarity between user vector and all item vectors
    cosine_scores = cosine_similarity(user_vector, item_vectors).flatten()
    
    # Add scores to our dataframe
    df['Similarity_Score'] = cosine_scores
    
    # Step 3 & 4: Sorting and Filtering (Top-N List)
    # Sort in descending order to push highest matches to the top
    top_matches = df.sort_values(by='Similarity_Score', ascending=False).head(top_n)
    
    return top_matches

if __name__ == "__main__":
    # Load the dataset
    dataset = load_data('raw_skills.csv')
    
    if dataset is not None:
        print("--- Digital Matchmaker: Tech Stack Recommender ---")
        print("Enter your skills OR a target job role (e.g., Python, Cloud OR Frontend Developer)")
        
        # Step 1: Ingestion (Capture User State)
        user_input = input("Your Input: ")
        
        # Ensure we have data to process
        if len(user_input.strip()) > 0:
            print("\nCalculating vector alignments...\n")
            
            # Execute Pipeline
            recommendations = get_recommendations(user_input, dataset, top_n=3)
            
            # Output the Top-N List
            print("--- Top Career Path Recommendations ---")
            for index, row in recommendations.iterrows():
                # Format score as a percentage match
                match_percentage = round(row['Similarity_Score'] * 100, 2)
                
                # Only show relevant matches
                if match_percentage > 0:
                    print(f"Role: {row['Role']}")
                    print(f"Match Score: {match_percentage}%")
                    print(f"Key Skills: {row['Skills']}")
                    print("-" * 40)
                elif index == recommendations.index[0]:
                    print("No strong matches found. Try entering different skills.")
        else:
            print("Error: Minimum input required to run similarity math.")