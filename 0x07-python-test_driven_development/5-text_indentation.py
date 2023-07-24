#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    separators = ['.', '?', ':']
    current_sentence = ''
    
    for char in text:
        current_sentence += char
        
        if char in separators:
            print(current_sentence.strip())
            current_sentence = ''

    if current_sentence:
        print(current_sentence.strip())
