from textops import clean_text, word_tokens
s = "  I like python  "
clean_text(s)
word_tokens("I like python")
print(clean_text(" \mI lovve python!!  ")) 
print(word_tokens("I love python"))
