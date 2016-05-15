import re
import nltk

from nltk.tokenize import WhitespaceTokenizer
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree


# Utilizado para retornar as entidades nomeadas de nome completo (ex: "Barack Obama" ao invés de "Barack" e "Obama")
def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []

    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    return continuous_chunk

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
        named_entities.append([token for token, pos in sent3[i].leaves()])
        #print sent3[i].leaves()[0][0]
print indexes

#print get_continuous_chunks(content)

print named_entities

# A ideia é buscar as entidades nomeadas e através do regex tokenize (ou algum outro) buscar no texto as posições de cada uma