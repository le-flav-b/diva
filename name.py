'''
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint


links = ["https://www.listedemots.com/liste-prenoms"] + \
        ["https://www.listedemots.com/liste-prenoms_page-" + str(i) for i in range(2, 23)]
names = []

for link in links:
    names += [span.text for span in bs(requests.get(link).content, 'html.parser').find('article').find_all('span', class_='mot')]

good_names = ['Alva', 'Alvana', 'Avara', 'Aviva', 'Diva', 'Dova', 'Evana', 'Godiva', 'Iva', 'Ivana', 'Ivanna', 'Jova', 'Jovana', 'Lévana', 'Loéva', 'Naéva', 'Nava', 'Niva', 'Nova', 'Réva', 'Seva', 'Silva', 'Teva', 'Valda', 'Valia', 'Vana', 'Vania']

names_2_syl = ['Alva', 'Diva', 'Dova', 'Iva', 'Jova', 'Nava', 'Niva', 'Nova', 'Réva', 'Seva', 'Silva', 'Teva', 'Valda', 'Valia', 'Vana', 'Vania']


good_name_2_syl = ['Alva', 'Diana', 'Diva', 'Dova', 'Jova', 'Niva', 'Nova', 'Seva', 'Valia', 'Vana', 'Vania']

words = {
    'a': ['assistant', 'agent', 'algorithm', 'artificial', 'AI'],
    'd': ['digital', 'domotics'],
    'e': ['embedded'],
    'i': ['interactive', 'information', 'IT', 'information'],
    'j': [],
    'l': ['live', 'local', 'le flav'],
    'n': ['numerical'],
    'o': ['order', 'optimization', 'on-board'],
    's': ['software', 'script', 'safety', 'system'],
    'v': ['voice', 'virtual']
}

pprint(words)
print()
print('Diva ->  Domotics and Inquiries by Voice Assist')
print('Diva ->  Domotics and Interrogations by Voice Assist')
'''
print('Diva ->  Domotics and Information by Voice Assistance')
'''
print('Diva ->  D I Voice Assistant')
print('Diva ->  Domotics Inquiries V A')
print('Diva ->  Digital I V A')
print('Diva ->  D Interactive V A')
print('Diva ->  D Iinformation V A')
print('Diva ->  D I Virtual Agent')
print('Diva ->  D I V Algorithm')
print('Diva ->  D I V AI')
'''
