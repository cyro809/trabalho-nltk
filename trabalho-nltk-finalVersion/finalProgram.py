import re
import nltk
import os
import sys as Sys

from nltk.tokenize import WhitespaceTokenizer
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from nltk.tokenize.util import regexp_span_tokenize

finalArticles = []
articleName = input("Insira o nome do arquivo: ")
textName = input("Insira o nome da pasta para os textos: ")
entitiesName = input("Insira o nome da pasta as entidades nomeadas: ")    

def fillFinalArticles(filename):
	content = open(filename, 'r').read()
	articles = re.sub('<.*?>', '##', content).split('##')
	new_articles = [article.strip() for article in articles if not article.strip() == '']
	
	for i in range(len(new_articles)):
	    finalArticles.append(new_articles[i].split('\n', 1))
	    
#FillfinalArticles and create dir:	
fillFinalArticles(articleName)
os.makedirs(textName, exist_ok = True)
os.makedirs(entitiesName, exist_ok = True)

#Start the program:
for item in finalArticles:
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    
    indexes = sent_tokenizer.span_tokenize(item[1]) # Indices de sentenca

    sent1 = nltk.word_tokenize(item[1])
    sent2 = nltk.pos_tag(sent1)
    sent3 =  nltk.ne_chunk(sent2, binary = True)

    named_entities = []
    for i in range(len(sent3)):
        if "NE" in str(sent3[i]):
            named_entities.append(' '.join(token[0] for token in sent3[i].leaves()))

    #------------------------------------------#
    #If we want to remove repeated entities:
    #seen = set()
    #named_entitiesFinal = []
    #for item in named_entities:
    #    if item not in seen:
    #        seen.add(item)
    #        named_entitiesFinal.append(item)
    #------------------------------------------#

    word_indexes = []
    for token in named_entities:
        index = item[1].find(token)
        word_indexes.append((index, index+len(token)))

    #Writing the files:
    f_name = item[0] + '.txt'
    f = open(textName + "/" + f_name, 'w')
    f.write(item[1][1:])
    f.write("\n\n")

    for i in range(len(indexes)):
            f.write(str(indexes[i]) + " ")

    f.write("\n\n")
    for i in range(len(word_indexes)):
            f.write(str(word_indexes[i]) + " ")

    f_name = "NE - " + item[0] + ".txt"
    f = open(entitiesName + "/" + f_name, 'w')
    for name in named_entities:
        f.write(name + "\n")
        
        
        
