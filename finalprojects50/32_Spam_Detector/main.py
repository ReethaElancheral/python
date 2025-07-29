# spam_detector.py

import re
import os
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class Classifier:
    def __init__(self, model_file='spam_model.pkl', vector_file='vectorizer.pkl'):
        self.model_file = model_file
        self.vector_file = vector_file
        self.model = None
        self.vectorizer = None

    def preprocess(self, text):
        text = text.lower()
        text = re.sub(r'[^a-z0-9\s]', '', text)
        return text

    def load_model(self):
        if not os.path.exists(self.model_file) or not os.path.exists(self.vector_file):
            raise FileNotFoundError("Model or vectorizer not found. Please train first.")
        with open(self.model_file, 'rb') as f:
            self.model = pickle.load(f)
        with open(self.vector_file, 'rb') as f:
            self.vectorizer = pickle.load(f)

    def train(self, texts, labels):
        self.vectorizer = CountVectorizer()
        X = self.vectorizer.fit_transform([self.preprocess(t) for t in texts])
        self.model = MultinomialNB()
        self.model.fit(X, labels)
        with open(self.model_file, 'wb') as f:
            pickle.dump(self.model, f)
        with open(self.vector_file, 'wb') as f:
            pickle.dump(self.vectorizer, f)
        print("✅ Model trained and saved.")

    def predict(self, text):
        if not self.model or not self.vectorizer:
            self.load_model()
        X = self.vectorizer.transform([self.preprocess(text)])
        return self.model.predict(X)[0]

    def predict_generator(self, messages):
        for msg in messages:
            yield msg, self.predict(msg)

def load_training_data(filepath='spam_data.txt'):
    if not os.path.exists(filepath):
        raise FileNotFoundError("Training file not found.")
    texts, labels = [], []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                labels.append(parts[0])
                texts.append(parts[1])
    return texts, labels

def main():
    clf = Classifier()

    while True:
        print("\n📧 Spam Detector")
        print("1. Train Model")
        print("2. Test Message")
        print("3. Test Multiple Messages")
        print("4. Exit")
        choice = input("Choose option: ")

        try:
            if choice == '1':
                texts, labels = load_training_data()
                clf.train(texts, labels)
            elif choice == '2':
                msg = input("Enter message: ")
                result = clf.predict(msg)
                print(f"Prediction: {'📬 Spam' if result == 'spam' else '📥 Not Spam'}")
            elif choice == '3':
                print("Enter messages (type 'done' to finish):")
                messages = []
                while True:
                    line = input("> ")
                    if line.lower() == 'done':
                        break
                    messages.append(line)
                for msg, res in clf.predict_generator(messages):
                    print(f"[{res.upper()}] - {msg}")
            elif choice == '4':
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()

