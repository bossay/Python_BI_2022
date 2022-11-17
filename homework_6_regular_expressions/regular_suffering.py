import requests
import re
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

# Expand the file using regular expressions and write all ftp-links from there into the file
references = requests.get('https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references').content
ftps = re.findall(r'ftp[/\w#.]*[.\w*]', references.decode('utf-8'))
with open('ftps.txt', 'w') as file:
    file.write('\n'.join(ftps) + '\n')

# Extract all the numbers from the story
story = requests.get('https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD').content
number_story = re.findall(r'\d*\.\d+|\d+', story.decode('utf-8'))

# Extract from the story all the words that have the letter 'a' in them
aaa_story = re.findall(r'\b\w*[Aa]\w*\b', story.decode('utf-8'))

# Extract all exclamatory sentences from the story
exc_story = re.findall(r'[A-Z][^.?!]*!', story.decode('utf-8'))

# Histogram of the distribution of the lengths of unique words
word_story = re.findall(r'\b[\w\'-]+\b', story.decode('utf-8'), re.UNICODE)
unique_words = set(list(map(lambda x: x.lower(), word_story)))

length_of_words = {}
for word in unique_words:
    if len(word) not in length_of_words:
        length_of_words[len(word)] = 1
    else:
        length_of_words[len(word)] += 1

sum_of_lengths = sum(length_of_words.values())
for len_word in length_of_words:
    length_of_words[len_word] = round(length_of_words[len_word] / sum_of_lengths, 5)

# Create bar-plot
fig, ax = plt.subplots(figsize=(10, 5))
plt.bar(length_of_words.keys(), length_of_words.values())
plt.title('Unique words length distributions', size=16)
plt.xlabel('Word length', size=10)
plt.ylabel('Share of words with a certain length among unique words', size=10)
ax.xaxis.set_major_locator(tck.MultipleLocator(1))
ax.tick_params(width=1, length=5, labelsize=10)
plt.show()


# Translator function from the brick language
def brick(string):
    re.sub(r'([ауоыэяюёие])', r'\1к\1', string, flags=re.IGNORECASE)
