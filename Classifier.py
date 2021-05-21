import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import time 


class Classifier:

    def __init__(self, filename="quizdb_classifier_training_data.json"):
        self.vectorizer = pickle.load(open('vectorizer.pkl'))
        self.category_classifier = pickle.load(open('category.pkl'))
        self.subcategory_classifier = pickle.load(open('subcategory.pkl'))

    def predict_categories(self, questions):
        X = self.vectorizer.transform([q.content() for q in questions])
        return self.category_classifier.predict(X)

    def predict_subcategories(self, questions):
        X = self.vectorizer.transform([q.content() for q in questions])
        return self.subcategory_classifier.predict(X)
