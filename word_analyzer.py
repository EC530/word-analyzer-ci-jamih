from matplotlib import pyplot as plt
import re

# Function for reading words from text file
# And displaying word frequency in histogram
def txt_count_words(n):
    f = open(n, "r")

    # Create an empty dictionary
    d = dict()

    # Loop through each line of the file
    for line in f:
        # Convert the characters in line to uppercase
        # to avoid case mismatch
        line = line.upper()

        # using res to filter string and extract punctuation and symbols
        res = re.findall(r'\w+', line)

        # Iterate over each word in line
        for word in res:
            # Check if the word is already in dictionary
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
