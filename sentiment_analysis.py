import string
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Downloading required libraries
# nltk.download('vader_lexicon')
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# Initializing SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


class SentimentAnalysis:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = self.read_file()
        self.processed_text = self.process_text()
        self.sentiments = self.analyze_sentiment()

    def read_file(self):
        try:
            with open(self.file_path, encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print("Error: File not found")
            return ""

    def process_text(self):
        # Remove punctuation
        text = self.text.translate(str.maketrans("", "", string.punctuation))

        # Tokenize the text
        tokens = word_tokenize(text)

        # Convert to lower case
        tokens = [w.lower() for w in tokens]

        # Remove stop words
        tokens = [w for w in tokens if w not in stop_words]

        # Perform word stemming
        tokens = [lemmatizer.lemmatize(w) for w in tokens]

        return " ".join(tokens)

    def analyze_sentiment(self):
        # Analyze the sentiment of the processed text
        sentiments = []
        words = word_tokenize(self.processed_text)
        for word in words:
            # Analyzing the sentiment intensity of each word
            score = sia.polarity_scores(word)
            sentiments.append(score)
        return sentiments

    def classify_sentiment(self):
        # Classifying the overall sentiment
        compound = 0.0
        for sentiment in self.sentiments:
            compound += sentiment['compound']
        if compound >= 0.05:
            return "Positive"
        elif compound <= -0.05:
            return "Negative"
        else:
            return "Neutral"


if __name__ == "__main__":
    file_path = "read.txt"
    analysis = SentimentAnalysis(file_path)
    # print("Sentiments of each word:", analysis.sentiments)
    print("Overall sentiment:", analysis.classify_sentiment())

