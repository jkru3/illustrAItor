import json

file = open("message.txt")
c = (file.read())
cjson = json.loads(c)
titles = ["The Maze Runner", "The Hunger Games", "Harry Potter and The Chamber of Secrets", "Fahrenheit 451"]


# Return existing book titles as a numbered list in a string array.
def get_titles():
    return titles


# Print the content in a number list format.
def numbered_print(txt):
    idx = 1
    for s in txt:
        print(f"{idx}. {s}")
        idx = idx + 1


# Split the paragraphs into sentences and return as an array of strings.
def split_paragraph(paragraph):
    sentences = paragraph.split(". ")
    return sentences


# Get the content of the book by title.
def get_book_by_title(title):
    book = cjson[title]
    return book


# Get the content of the book by index starting at 0.
def get_book_by_index(idx):
    currentTitle = titles[idx]
    book = cjson[titles[idx]]
    return book


# Get the sentence of the book by index
def get_book_sentence(title, idx):
    book = get_book_by_title(title)
    sentences = split_paragraph(book)
    return sentences[idx]


### Return the title's best sentences as an array of strings.
def get_best_sentences(title):
    bestIdx = []
    if title == "The Maze Runner":
        bestIdx.append(0)
        bestIdx.append(1)
        bestIdx.append(2)
    elif title == "The Hunger Games":
        bestIdx.append(1)
        bestIdx.append(2)
        bestIdx.append(7)
    elif title == "Harry Potter and The Chamber of Secrets":
        bestIdx.append(1)
        bestIdx.append(2)
        bestIdx.append(3)
    elif title == "Fahrenheit 451":
        bestIdx.append(0)
        bestIdx.append(1)
        bestIdx.append(3)
    bestSentences = []
    for i in bestIdx:
        bestSentences.append(get_book_sentence(title, i))
    return bestSentences


print(split_paragraph(get_book_by_index(3)))
print("--------------")
print(get_best_sentences(titles[3]))
