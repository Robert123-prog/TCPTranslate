import socket
import os
from googletrans import Translator

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 6969))

languages = {}
with open('languages', 'r', encoding='utf-8') as f:
    for line in f:
        # dai split dupa space => lista
        parts = line.split()

        language_name = ' '.join(parts[:-1])
        abbreviation = parts[-1] #ultimu part din rand = abrevierea

        languages[language_name] = abbreviation

translator = Translator()

s.listen()
cs, addr = s.accept()

phrase = cs.recv(1000).decode('utf-8') #trebe decodat


print('Please use one of the following abbreviations: ')
print(languages)
language_to_translate_to = input('Enter the language code to translate to: ')


detected = translator.detect(phrase)
translation = translator.translate(phrase, src=detected.lang, dest=language_to_translate_to)

cs.send(translation.text.encode('utf-8'))  # encodezi la loc

cs.close()

# while True:
#     s.listen()
#     cs, addr = s.accept()
#
#     if os.fork() == 0:
#         s.close() #inchizi socketu "parent"
#
#         phrase = cs.recv(1000).decode('utf-8') #trebe decodat
#
#         language_to_translate_to = input('Enter the language code to translate to: ')
#
#         detected = translator.detect(phrase)
#         translation = translator.translate(phrase, src=detected.lang, dest=language_to_translate_to)
#
#         cs.send(translation.text.encode('utf-8'))  # encodezi la loc
#
#         cs.close()
#     else:
#         cs.close()

