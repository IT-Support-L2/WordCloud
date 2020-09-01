# importing necessary modules

import re
from wordcloud import WordCloud, STOPWORDS

# path of your txt file
path = "C:/Users/user/Desktop/my_folder/my_text.txt"


text = open(path, encoding='utf-8')

# using text.read() method to return string
new_text = text.read()

# delete all punctuations using regex and re.sub from python re module
res = re.sub(r'[^\w\s]', '', new_text) 

# splitting each word apart
new_t = res.split()


# unwanted words to delete from text
un_words = ["the", "also", "after", "before", "on", "even", "not", "only", "in", "all", "same", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

# deleting unwanted words using list comprehension
resultwords  = [word for word in new_t if word.lower() not in un_words] 

# joining each word
result = ' '.join(resultwords)

dictionary = {}

lst = result.split()

# count words frequencies and append each word with its frequency count into the dictionary
for elements in lst:  
    
    if elements in dictionary: 
        dictionary[elements] += 1
    else: 
        dictionary.update({elements: 1})

# generate image from words frequencies dictionary

cloud = WordCloud(background_color = "white", max_words = 5000, stopwords = set(STOPWORDS))
cloud.generate_from_frequencies(dictionary)
cloud.to_file("wordCloud.png")
