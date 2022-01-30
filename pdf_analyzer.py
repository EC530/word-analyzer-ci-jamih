import pdfplumber
from matplotlib import pyplot as plt
import re


def pdf_count_words(n):
    pdf = pdfplumber.open(n)
    page = pdf.pages[0]
    # extracting text from pdf
    # as a string

    text = page.extract_text()
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
    res = re.findall(r'\w+', text)

    for i in res:
        word = i.lower()
        # Check if the word is already
        # in the dictionary
        if word not in stop_words:
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1

    pdf.close()
    return d


def pdf_histogram(d):
    # Create an empty array for words
    words = []

    # Create an empty array for frequency
    # of words
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
    plt.title('Word Frequency in poem.pdf')

    plt.xticks(
        rotation=45,
        horizontalalignment='right',
        fontweight='light',
        fontsize='small'
    )
    plt.tight_layout()
    plt.show()
    return words, freq


def main():
    d = pdf_count_words('poem.pdf')
    pdf_histogram(d)


if __name__ == '__main__':
    main()
