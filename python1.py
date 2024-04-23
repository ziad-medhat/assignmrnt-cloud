import nltk
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

with open('paragraphs.txt', 'r') as file:
    text = file.read()

# text into words
words = nltk.word_tokenize(text)

# Remove stop words
stop_words = set(nltk.corpus.stopwords.words('english'))
filtered_words = [word.lower() for word in words if word.lower() not in stop_words and word.isalnum()]

# Count the frequency of each word
word_freq = Counter(filtered_words)

# Display word frequency count
for word, freq in word_freq.items():
    print(f'{word}: {freq}')