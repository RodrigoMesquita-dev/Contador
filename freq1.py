import requests
from bs4 import BeautifulSoup
import operator
import pandas as pd
from collections import Counter

def one_link(link):
    source_code = requests.get(link).text
    soup = BeautifulSoup(source_code, 'html.parser')

    wordlist = []
    clean_list = []
    word_count = {}

    words = soup.text.lower().split()
    for each_word in words:
        wordlist.append(each_word)

    word_count = clean_wordlist(words)

    df = pd.DataFrame(word_count.items(), columns=['Palavra', 'Frequência'])

    symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/.,"
    titlename = soup.title.text
    for i in range(len(symbols)):
        titlename = titlename.replace(symbols[i], '')
    filename = titlename+'.xlsx'
    df.sort_values(by=['Frequência'],ascending=[False]).to_excel(filename, index = False)


def many_links(links):
    geral = {}
    for link in links:
        source_code = requests.get(link).text
        soup = BeautifulSoup(source_code, 'html.parser')
        wordlist = []
        words = soup.text.lower().split()
        for each_word in words:
            for i in range(len(symbols)):
                each_word = each_word.replace(symbols[i], '')
            if len(each_word) > 0:
                wordlist.append(each_word)
        
        word_count = {}
        word_count = create_dictionary(wordlist)

        for word in words:
            if word in geral:
                geral[word] += word_count[word]
            else:
                geral[word] = word_count[word]

        df = pd.DataFrame(word_count.items(), columns=['Palavra', 'Frequência'])

        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/.,"
        titlename = soup.title.text
        for i in range(len(symbols)):
            titlename = titlename.replace(symbols[i], '')
        filename = titlename+'.xlsx'
        df.sort_values(by=['Frequência'],ascending=[False]).to_excel(filename, index = False)

    df = pd.DataFrame(geral.items(), columns=['Palavra', 'Frequência'])
    df.sort_values(by=['Frequência'],ascending=[False]).to_excel('geral.xlsx', index = False)
    

    
def create_dictionary(clean_list):
    word_count = {}
 
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    
    return word_count
    #print(df.sort_values(by=['Frequência'],ascending=[False]))
    #df.sort_values(by=['Frequência'],ascending=[False]).to_excel('saved_file.xlsx', index = False)



def clean_wordlist(wordlist):
    clean_list = []
    
    for word in wordlist:
        symbols = "!@#$%^&*()_+={[}]|\;:\"<>?/.,"
 
        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')
 
        if len(word) > 0:
            clean_list.append(word)

    return create_dictionary(clean_list)

def verify_link(lnk):
    site_list = []
    site_list = lnk.split()
    if len(site_list) > 1:
        many_links(site_list)
    else:
        one_link(lnk)



url = input("Digite o link do site, ou sites separados por espaço: \n")

verify_link(url)