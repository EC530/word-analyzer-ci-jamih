from matplotlib import pyplot as plt
import re


def txt_count_words(n):
    # Function for reading words from text file
    # And displaying word frequency in histogram
    f = open(n, "r")

    # Create an empty dictionary
    d = dict()

    # Array of NLTK English Stopwords
    stop_words = ["i", "me", "my", "myself", "we",
                  "our", "ours", "ourselves", "you",
                  "your", "yours", "yourself", "yourselves",
                  "he", "him", "his", "himself", "she", "her",
                  "hers", "herself", "it", "its", "itself", "they",
                  "them", "their", "theirs", "themselves", "what",
                  "which", "who", "whom", "this", "that", "these",
                  "those", "am", "is", "are", "was", "were", "be",
                  "been", "being", "have", "has", "had", "having",
                  "do", "does", "did", "doing", "a", "an", "the",
                  "and", "but", "if", "or", "because", "as", "until",
                  "while", "of", "at", "by", "for", "with", "about",
                  "against", "between", "into", "through", "during",
                  "before", "after", "above", "below", "to", "from",
                  "up", "down", "in", "out", "on", "off", "over",
                  "under", "again", "further", "then", "once", "here",
                  "there", "when", "where", "why", "how", "all", "any",
                  "both", "each", "few", "more", "most", "other", "some",
                  "such", "no", "nor", "not", "only", "own", "same", "so",
                  "than", "too", "very", "s", "t", "can", "will", "just",
                  "don", "should", "now"]

    # Loop through each line of the file
    for line in f:
        # Convert the characters in line to lowercase
        # to avoid case mismatch
        line = line.lower()

        # using res to filter string and extract punctuation and symbols
        res = re.findall(r'\w+', line)

        # Iterate over each word in line
        for word in res:
            # Check if the word is already in dictionary
            # Only put word in dictionary if not a stop word
            if word not in stop_words:
                if word in d:
                    # Increment count of word by 1
                    d[word] = d[word] + 1
                else:
                    # Add the word to dictionary with count 1
                    d[word] = 1

    return d


def txt_histogram(d):
    # Create an empty array for words
    words = []
    # Create an empty array for frequency of words
    freq = []
    # Print the contents of dictionary
    for key in list(d.keys()):
        print(key, ":", d[key])
        words.append(key)
        freq.append(d[key])

    print(words)
    print(freq)

    # Creating Histogram from data

    width = 0.7
    plt.bar(words, freq, width)
    plt.xlabel('Word')
    plt.ylabel('Word Frequency')
    plt.title('Word Frequency in poem.txt')

    plt.xticks(
        rotation=45,
        horizontalalignment='right',
        fontweight='light',
        fontsize='small'
    )
    plt.tight_layout()
    plt.show()


def main():
    d = txt_count_words('poem.txt')
    txt_histogram(d)


if __name__ == '__main__':
    main()
