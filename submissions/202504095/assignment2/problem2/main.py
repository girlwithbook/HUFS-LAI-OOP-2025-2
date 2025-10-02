textops/
  __init__.py        
  main.py              
  clean/
    __init__.py
    filters.py        
  tokenize/
    __init__.py
    word.py         
from textops import clean_text, word_tokens
s = "  I like python  "
clean_text(s)
word_tokens("I like python")

