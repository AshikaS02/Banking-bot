import nltk
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

f=open('comments.txt','r',errors='ignore')
read=f.read()
read=read.lower()
nltk.download('punkt')
nltk.download('wordnet')
st=nltk.sent_tokenize(read)
wt=nltk.word_tokenize(read)

lem=nltk.stem.WordNetLemmatizer()

gin=("hello","hi","greetings","what's up","hey")
grs=["hi","hey","hi there","hello","I am glad! you are talking to me"]

def Lemtok(tokens):
    return [lem.lemmatize(token) for token in tokens]
rem=dict((ord(pun),None) for pun in string.punctuation)

def Lemnor(text):
    return (nltk.word_tokenize(text.lower().translate(rem)))



def greeting(resword):
    for word  in resword.split():
        if word.lower() in gin:
            return random.choice(grs)

def resp(resus):
    botres=""
    st.append(resus)
    tvic=TfidfVectorizer(tokenizer=Lemnor,stop_words='english')
    tfidf=tvic.fit_transform(st)
    vals=cosine_similarity(tfidf[-1],tfidf)
    idx=vals.argsort()[0][-2]
    flat=vals.flatten()
    flat.sort()
    req_tfidf=flat[-2]
    if (req_tfidf==0):
        botres=botres+"I am sorry I don't understand you"
        return botres
    else:
        botres=botres+st[idx]
        return botres


def chatbot(ures):
    ures=ures.lower()
    if (ures!="bye"):
        if(ures=="thanks" or ures=='thank you'):
            return ("You are welcome")
        else:
            if (greeting(ures)!=None):
                return (greeting(ures))
            else:
                # print("Chatbot:", end='')
                # st.remove(ures)
                return (resp(ures))

    else:
        return ("Bye! See you Soon")
