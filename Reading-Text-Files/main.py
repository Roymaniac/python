# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # open text
    read_file = open(filename, 'r')
    # read text file
    output = read_file.read()
    # close the file
    read_file.close()
    # return the output of the file
    return output


def count_words():
    # variable text calls the read_file function & hold the file content
    text = read_file_content("./story.txt")
    # split & return each word in lowercase then get stored as list/array
    destructured_sentence = text.lower().split()
    # loop through the destructured list/array
    for word in destructured_sentence:
        # get the no of occurrence of a particular word in the list
        no_of_count = text.count(word)
        # create and empty dictionary/object
        dictionary = {}
        # store each word as a key and the no of occurrence as it value
        dictionary[word] = no_of_count
        # output the dictionary/object
        print(dictionary)


# function call
count_words()
