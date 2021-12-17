import nltk
from nltk.chat.util import Chat, reflections



pairs = [
    ["salut,cava,bonjour",["hello,salut toi , bonjour"]],
    ["(.*)aider",["oui je peux vous %1"]],
    ["je veux(.*)",["D'accord je veux vous le prepare "]],
    ["(.*)ville",["  Nous sommes a paris rue de france "]]
]

chat=Chat(pairs,reflections)
chat.converse()