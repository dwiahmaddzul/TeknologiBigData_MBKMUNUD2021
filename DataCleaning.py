import numpy as np
import pandas as pd

#import seaborn as sns
import matplotlib.pyplot as pyplot

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.stem import LancasterStemmer,WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

import re,string,unicodedata
from string import punctuation
from wordcloud import WordCloud,STOPWORDS

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

#Read
df = pd.read_json('Hasil\result.json',encoding="ISO-8859-1")
df.head()

kamus_alay = pd.read_csv('/content/drive/My Drive/colab/new_kamusalay.csv', encoding='latin-1', header=None)
kamus_alay = kamus_alay.rename(columns={0: 'alay', 
                                      1: 'baku'})

"""Perintah diatas merupakan inisiasi untuk membaca kamus alay kemudian perintah beriktutnya
 mengganti kolom dengan indeks terurut menjadi string (dictionary list)"""

kamus_stopword = pd.read_csv('/content/drive/My Drive/colab/stopwordbahasa.csv', header=None)
kamus_stopword = kamus_stopword.rename(columns={0: 'stopword'})


"""Perintah diatas merupakan inisiasi untuk membaca kamus stopword kemudian perintah beriktutnya
 mengganti kolom dengan indeks terurut menjadi string (dictionary list)"""

emoji = pd.read_csv('/content/drive/My Drive/colab/Emoticon.csv', encoding="ISO-8859-1", header=None)
emoji = emoji.rename(columns={0: 'hexa',
                              1: 'arti'})

"""Perintah diatas merupakan inisiasi untuk membaca kamus emoji kemudian perintah beriktutnya
 mengganti kolom dengan indeks terurut menjadi string (dictionary list)"""

kamus_noemoji =  pd.read_csv('/content/drive/My Drive/colab/bytemoaja.csv', encoding='latin-1', header=None)
kamus_noemoji = kamus_noemoji.rename(columns={0: 'byte', 
                                      1: 'hapus'})

"""Perintah diatas merupakan inisiasi untuk membaca kamus noemoji kemudian perintah beriktutnya
 mengganti kolom dengan indeks terurut menjadi string (dictionary list)"""

def casefolding(text):
    text = re.sub(r'@\S+', '',text)
    return text.lower()

df['content'] = df['content'].apply(casefolding)

"""Perintah diatas mendefinisikan fungsi untuk mengubah kata menjadi berkarakter huruf kecil semua
proses ini dinamakan casefolding. Parameter text yang digunakan akan diubah (return) menjadi lower"""

df.isna().sum()
"""Penerapan library pandas adalah untuk menghitung jumlah nilai yang luput dari pengisian nilai
dengan menampilkan jumlah missing value dari tiap kolom parameter 'Ujaran Kebencian'"""

df['content']
"""Perintah diatas untuk menampilkan sebagian isi tweet"""

print("Ukuran: ", kamus_alay.shape)
kamus_alay.head(15)
#"""Perintah diatas untuk menampilkan ukuran dan sebagian data kamus alay"""

print("Ukuran: ", kamus_noemoji.shape)
kamus_noemoji.head(15)

print("Ukuran: ", kamus_stopword.shape)
kamus_stopword.head(15)

print("Ukuran: ", emoji.shape)
emoji.head(15)

###############################
#def casefolding(text):
#    return text.lower()

def hapus_karakter_useless(text):
    text = re.sub('\n',' ',text) # Hapus '\n'
    text = re.sub('rt',' ',text) # Hapus simbol retweet    
    #text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))',' ',text) # Hapus URL
    text = re.sub(' locator ',' ',text) # Menghapus kata locator
    text = re.sub(' resource ',' ',text) # Hapus kata resource
    text = re.sub(' user ',' ',text) # Hapus sibol user
    text = re.sub('warga tiktok',' ',text) # Hapus sibol user
    text = re.sub(' url ',' ',text) # Hapus kata uniform
    text = re.sub(' gue ',' ',text) # Hapus kata uniform
    text = re.sub(' iya ',' ',text) # Hapus kata uniform
    text = re.sub(' amp ',' ',text) # Hapus kata uniform
    text = re.sub(' ya ',' ',text) # Hapus kata uniform
    text = re.sub(' sih ',' ',text) # Hapus kata uniform
    text = re.sub(' pas ',' ',text) # Hapus kata uniform
    text = re.sub(' ng ',' ',text) # Hapus kata uniform
    text = re.sub(' sa ',' ',text) # Hapus kata uniform
    text = re.sub(' rak ',' ',text) # Hapus kata uniform
    text = re.sub(' uniform ',' ',text) # Hapus kata uniform
    text = re.sub('  +', ' ', text) # Hapus spasi lebih
    return text
    
    
def hapuslink(text):
    text = re.sub(r'http\S+', '',text)
    return text

def hapus_nonalpanumerik(text):
    text = re.sub('[^0-9a-zA-Z]+', ' ', text) 
    return text

map_emoji = dict(zip(emoji['hexa'], emoji['arti']))

def convert_emot(text):
    return ' '.join([map_emoji[word] if word in map_emoji else word for word in text.split(' ')])
##### COBA

"""map_noemoji = dict(zip(kamus_noemoji['hexa'], emoji['arti']))

def convert_emot(text):
    return ' '.join([map_emoji[word] if word in map_emoji else word for word in text.split(' ')])
"""
##### COBA

# def cleansing_emothex(text):
#     text = text.decode('iso-8859-9').encode('utf-8')
#     return text

def cleaning(text):
    text = hapus_nonalpanumerik(text) # 2
    text = hapus_karakter_useless(text) # 2
    return text

print("lowercase: ", casefolding("Halooo, duniaa!"))
print(b'\xF0\x9F\x80\x84'.hex())
print("remove_nonaplhanumeric: ", hapus_nonalpanumerik("Halooo,,,,, duniaa!!"))
print("remove_unnecessary_char: ", hapus_karakter_useless("Hehe\n\n rt USER USER uniform apa kabs www.google.com\n  hehe"))

"""

"""

# df['Tweet'] = df['Tweet'].apply(cleaning)
map_kamus_alay = dict(zip(kamus_alay['alay'], kamus_alay['baku']))

def normalisasi(text):
    return ' '.join([map_kamus_alay[word] if word in map_kamus_alay else word for word in text.split(' ')])

print("normalize_alay: ", normalisasi("aamiin adek abis 3x"))

# df['Tweet'] = df['Tweet'].apply(normalisasi)

map_katauseless = dict(zip(kamus_noemoji['byte'], kamus_noemoji['hapus']))


def normalisasinoemoji(text):
    return ' '.join([map_katauseless[word] if word in map_katauseless else word for word in text.split(' ')])

print("normalize_alay: ", normalisasinoemoji("x80 x8A anda sudah pergi jauh 3x"))

def hapus_stopword(text):
    text = ' '.join(['' if word in kamus_stopword.stopword.values else word for word in text.split(' ')])
    text = re.sub('  +', ' ', text) # Hapus spasi lebih
    text = text.strip()
    return text
print("remove_stopword: ", hapus_stopword("ada hehe adalah huhu yang hehe"))

# df['Tweet'] = df['Tweet'].apply(hapus_stopword)

factory = StemmerFactory()
stemmer = factory.create_stemmer()

def stemming(text):
    return stemmer.stem(text)
print("stemming: ", stemming("Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan"))

# df['Tweet'] = df['Tweet'].apply(stemming)

##export

new_dataframe = df.filter(['content'])
new_dataframe.to_csv('datakub22 .csv')

 """def clean_text(text):
   text = hapus_kurung(text)
   text = hapus_url(text)
   text = remove_special_characters(text, remove_digits=True)
   # text = stemmer(text)
   text = remove_stopwords(text)
   if (text=="br"):
     text=""
   return text"""

def preprocess(text):
    text = casefolding(text) # 1
    text = hapuslink(text) # 1
    text = hapus_nonalpanumerik(text) # 2
    text = hapus_karakter_useless(text) # 2
    text = normalisasi(text) # 3
    text = stemming(text) # 4
    text = normalisasinoemoji(text)#6 no EMOJI
    text = hapus_stopword(text) # 5
    return text

df['content'] = df['content'].apply(preprocess)

df['content'].head()

##export

new_dataframe = df.filter(['content'])


new_dataframe.to_csv('datakub2 .csv')


#plt.figure(figsize = (20,20))
#wc = WordCloud(max_words = 100 , width = 1600 , height = 800).generate(" ".join(df.content))
#plt.imshow(wc , interpolation = 'bilinear')


