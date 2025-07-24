
from recommender.outfit_recommender import OutfitRecommender

def main():
    recommender = OutfitRecommender("data/outfits.csv")
    print("Recommendations for color='Red', occasion='Party':")
    print(recommender.recommend(color='Black', occasion='Formal'))

if __name__ == "__main__":
    main()
