from collections import Counter
from more_itertools import flatten
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
import re
nltk.download('stopwords')

stopwords = nltk.corpus.stopwords.words('portuguese')

def stopwords_remove(text) -> list:
    """Retorna uma lista de listas em que cada lista inferior é composta por tokens sem a presença de stopwords."""
    # tokenização
    texts_list = list(map(str.split, text))

    # remoção de stopwords
    tokens_clean = []
    for text in texts_list:
        text_clean = [token for token in text if token not in stopwords]
        tokens_clean.append(' '.join(text_clean))

    return tokens_clean 

def clean_text(text) -> str:
    """Retorna uma string após remoção de ruídos"""
    CLEANR = re.compile('<.*?>')
    REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,.;]')
    
    text = str(text)
    text = text.lower()
    text = re.sub(CLEANR, ' ', text)
    text = REPLACE_BY_SPACE_RE.sub(' ', text)
    text = re.sub(r'\W+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'\d+', '', text)
    
    return text.strip()

def processing(text) -> list:
    """Retorna uma lista de listas em que cada lista inferior é composta por tokens."""
    titulos = list(map(clean_text, text))
    titulos = stopwords_remove(titulos)
    titulos = list(map(str.split, titulos))
    return titulos

def words_counting(text) -> dict:
    """Retorna um dicionário em que cada chave é uma palavra e o valor é a quantidade de vezes que a palavra se repete no corpus (text)."""
    return Counter(list(flatten(text)))

def plot_wordcloud(text) -> None:
    """Plota uman nuvem de palavras das palavras com maior frequência."""
    wordcloud = WordCloud(width=800, height=500,
                                max_font_size=230,
                                max_words=150,
                                background_color=None,
                                contour_color='black',
                                collocations=False).generate(' '.join(flatten(text)))
    
    plt.figure(figsize=(7, 5),facecolor='k', edgecolor='k')
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()