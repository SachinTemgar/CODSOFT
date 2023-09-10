import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

# Define a function to combine the features
def combine_features(data):
    return data['genres'] + ' ' + data['keywords'] + ' ' + data['tagline'] + ' ' + data['cast'] + ' ' + data['director']

# Load the dataset
dataset = pd.read_csv('D:\\X internship\\TASK NO 3\\movies.csv')

# Fill NA values with empty strings
for feature in ['genres', 'keywords', 'tagline', 'cast', 'director']:
  dataset[feature] = dataset[feature].fillna('')

# Apply the function to combine the features
dataset['combined_features'] = dataset.apply(combine_features, axis=1)

# Convert the text data to feature vectors
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(dataset['combined_features'])

# Calculate the similarity scores using cosine similarity
similarity_matrix = cosine_similarity(vectors)

def recommend_movies(title):
    # Find the closest match to the input movie title
    closest_match = difflib.get_close_matches(title, dataset['title'].tolist())[0]
    movie_idx = dataset[dataset.title == closest_match]['index'].values[0]

    # Get a list of similar movies
    similarity_scores = list(enumerate(similarity_matrix[movie_idx]))
    sorted_similar_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Return the titles of the top 20 similar movies
    return [dataset[dataset.index == i[0]]['title'].values[0] for i in sorted_similar_movies[:20]]
