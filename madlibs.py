# This program is going to read a story and ask user to replace key words from the story with their own words.

with open("story.txt", "r") as file:
    story = file.read()

target_begins="["
target_ends="]"
start_to_word=-1
words=set()

for position_of_word, word_in_position in enumerate(story):
    if word_in_position == target_begins:
        start_to_word = position_of_word
    
    if word_in_position == target_ends and start_to_word!=-1:
        word=story[start_to_word:position_of_word+1]
        words.add(word)
        start_to_word=-1
    
# print(words)
answers={}
for word in words:
    answer=input(f"Enter a word for {word}: ")
    answers[word]=answer
    
for word in words:
    story=story.replace(word, answers[word])

print(story)