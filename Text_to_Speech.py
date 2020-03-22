#DESCRIPTION: THIS PROGRAM TAKES TEXT FROM AN ONLINE ARTICLE AND CONVERTS THAT INTO SPEECH.

#Import the libraries
from newspaper import Article
import nltk
from gtts import gTTS
import os

#Get the article
article = Article('https://hackernoon.com/future-of-python-language-bright-or-dull-uv41u3xwx')

article.download() #Download the article
article.parse() #Parse the article
nltk.download('punkt') #Download the 'punkt' package
article.nlp() #Apply Natural Language Processing (NLP)

#Get the articles text
mytext = article.text

#Print the text
print(mytext)

# Language in which you want to convert
language = 'en' #English

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# read_article
myobj.save("read_article.mp3")

# Playing the converted file
os.system("start read_article.mp3")  
