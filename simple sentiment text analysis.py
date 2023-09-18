from textblob import TextBlob
from newspaper import Article

# Replace this URL with the direct URL of the article you want to analyze
url = 'https://www.example.com/news-article-url'

article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity  # -1 to 1
print(sentiment)
