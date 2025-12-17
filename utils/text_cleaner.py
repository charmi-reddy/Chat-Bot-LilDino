import string 

def clean_text(text):
    text=text.lower()
    return text.translate(str.maketrans("","",string.punctuation)).strip()