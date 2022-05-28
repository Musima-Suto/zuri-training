# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, 'r') as f:
        contents = f.read()
        return contents


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    list = text.split(" ")
    dict = {}
    word_count = 0  
    for item in list:
        if item in dict:
            dict[item] = dict[item] + 1
        
        else:
            dict[item] = 1
    for key, value in dict.items():
        print(f'{key}:{value}')
    
count_words()
