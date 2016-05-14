import re
import nltk

from nltk.tokenize import WhitespaceTokenizer


def split_articles():
	filename = "teste"
	content = open(filename, 'r').read()
	articles = re.sub('<.*?>', '##', content).split('##')
	new_articles = [article.strip() for article in articles if not article.strip() == '']

	for i in range(len(new_articles)):
		f_name = 'article{0}.txt'.format(i)
		f = open(f_name, 'w')
		f.write(new_articles[i])


filename = 'article1.txt'
content = open(filename, 'r').read()

sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
indexes = sent_tokenizer.span_tokenize(content) # Indices de sentenca

word_tokenizer = nltk.tokenize.api.StringTokenizer()
word_indexes = list(WhitespaceTokenizer().span_tokenize(content)) #indices de palavras


print word_indexes
print indexes