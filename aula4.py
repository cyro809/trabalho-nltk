import re
import nltk

from nltk.tokenize import WhitespaceTokenizer
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from nltk.tokenize.util import regexp_span_tokenize

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

sent1 = nltk.word_tokenize(content)
sent2 = nltk.pos_tag(sent1)
sent3 =  nltk.ne_chunk(sent2, binary=True)
named_entities = []

# Utilizado para retornar entidades nomeadas (Precisa de ajustes)
for i in range(len(sent3)):
    if "NE" in str(sent3[i]):
        named_entities.append(' '.join(token[0] for token in sent3[i].leaves()))



# word_indexes = [list(regexp_span_tokenize(content, re.compile("^(?!{0}).*$".format(token)))) for token in named_entities]

# print word_indexes
print
print indexes
print
print named_entities

# A ideia eh buscar as entidades nomeadas e atraves do regex tokenize (ou algum outro) buscar no texto as posicoes de cada uma