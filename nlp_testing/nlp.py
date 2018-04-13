import spacy
nlp = spacy.load('en')
doc = nlp(u'next bus to mandi from south')
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_,
	  # print(chunk.text)
          chunk.root.head.text)