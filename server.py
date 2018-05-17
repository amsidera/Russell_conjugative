# -*- coding: utf-8 -*-
import requests 
import nltk
from bs4 import BeautifulSoup 
from inspect import getsourcefile
from flask import Flask,  request
from flask_cors import CORS, cross_origin
from os.path import abspath, join, dirname


app = Flask(__name__, static_url_path='/settings')
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})

"""
We have to take out the vocabulary and the result of our analyzer to 
filter all the synonyms we get
"""
def dict_vocab ():
    dictio = {}
    full_filepath = join(dirname(abspath(getsourcefile(lambda:0))), "Analyzer")
    full_filepath = join(full_filepath, "output.vocab")
    with open(full_filepath, "r", encoding="utf-8" ) as f:
        text = f.readlines()
        for i in text: 
            i = i.split()
            dictio[i[0]]=i[1]
    return dictio


"""
We look for the synonymous in the dictionary and apply a threshold.
"""
def vocab (name, noun,lexicon_dictio):
    if (noun in lexicon_dictio) & (name in lexicon_dictio):
        polarity = float(lexicon_dictio[noun])
        polarity_sys = float(lexicon_dictio[name])
        threshold = 0.0001
        if ((polarity > threshold) & (polarity_sys > threshold)) | ((polarity< threshold) & (polarity_sys < threshold))  :
            return 1
        if ((polarity > -threshold) & (polarity < threshold)) & (polarity_sys> -threshold) & (polarity_sys < threshold)  :
            return 1 
        else: 
            return 0
    return 0
 
    
"""
We analyze each synonym of our word, in case it passes 
the filter we introduce it into our web page.
"""
def add (noun, lista, position):
    result = '</button><div id="text'+str(position)+'" class="dropdown-content">'
    for i in lista:                             
        result += str('<a onclick="mytoggle(this,dropdownclass'+str(position)+')">'+i+'</a>')
    result += '<a onclick="mytoggle2(this, '+str(position)+')" id="last'+str(position)+'">All</a>'
    result += str('</div></div>')
    return result

def synonyms(noun, position, lexicon_dictio, polarity):
    dictio ={}
    lista = []
    for syns in nltk.corpus.wordnet.synsets(noun):
        for l in syns.lemmas():
            if l.name().lower() != noun.lower():
                if l.name() not in dictio:
                    name = str(l.name()).replace("_", " ")
                    if polarity != 3:
                        back = vocab(name, noun, lexicon_dictio)
                        if back == 0 and polarity == 0:
                            lista.append(name)
                            dictio[l.name()]=1
                        if back == 1 and polarity == 1:
                            lista.append(name)
                            dictio[l.name()]=1
                    elif polarity == 3:
                        lista.append(name)
                        dictio[l.name()]=1
    if len(lista) != 0:
        result = add(noun, lista, position)
        boolean = 1
    else: 
        result = ''
        boolean = 0
    return result, boolean


"""
Translate to the language used by nltk
"""
def translate(position):
    if position == 0:
        return 'JJ'
    elif position == 1:
        return 'NN'
    elif position == 2:
        return 'RB'
    return 'JJ'

       
"""
Create the button in each of the adjectives that we have highlighted 
to display the synonyms
"""
def button(noun, sys, number):
    text_html = '<div id="'+str(number)+'" class="dropdown">'
    text_html +='<button onclick="iitbutton(\''+str(number)+'\')"'
    text_html += 'class="dropbtn"'
    text_html += 'id="dropdownclass'+str(number)+'">'+noun+sys
    return text_html


"""
Look at all the words and highlight the adjectives we have.
"""                   
def highlight(url, position_tag, polarity):
    f1 = open("settings/new.html")
    soup1 = BeautifulSoup(f1, 'html.parser')
    f1.close()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lexicon_dictio = dict_vocab()
    number = 0
    for artist in soup.find_all('p'):
        result = ''
        sent_text = nltk.sent_tokenize(artist.text)
        for sent in sent_text:
            tokens = nltk.word_tokenize(sent)
            tagged = nltk.pos_tag(tokens)
            position = 0
            for noun, tag in tagged:
                if tag == position_tag:
                    
                    sys1, boolean = synonyms(noun, number, lexicon_dictio, polarity)
                    if boolean == 1: 
                        text = button(noun, sys1, number)
                        result += text
                        number += 1
                    else: 
                        result += noun + ' '
                else: 
                    result += noun + ' '
                position +=1
        artist.replaceWith(BeautifulSoup(result, 'html.parser'))
    soup1.body.append(soup)

    return soup1

"""
Parameters of the server where we collect the variables that we need.
"""
@app.route('/', methods = ['POST', 'GET'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def worker():
    print(request.form['url'])
    position = translate(request.form['position'])
    polarity = float(request.form['polarity'])
    print(request.form['position'], position)
    print(request.form['polarity'])
    new_html = highlight(request.form['url'], position, polarity)
    
    return new_html.prettify()

@app.route('/settings', methods = ['GET', 'POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def worker1():
    f1 = open("new.js")
    soup_js = BeautifulSoup(f1, 'html.parser')
    f1.close()
#    script = soup_js.find('script')
#    print(script)
    return soup_js.prettify()
if __name__ == '__main__':

    app.run()

 
