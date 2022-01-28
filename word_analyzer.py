from matplotlib import pyplot as plt
import numpy as np
import re


def count_words(n):
    f = open(n, "r")
    #print(f.read())

    # Create an empty dictionary
    d = dict()
    
    # Loop through each line of the file
    for line in f:
        
    
        # Convert the characters in line to uppercase
        # to avoid case mismatch
        line = line.upper()
        '''
        # Remove the leading and trailing spaces
        line = line.strip()
    
        # Split the line into a list of words
        words = line.split(" ")
        '''
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
    
    # Print the contents of dictionary
    for key in list(d.keys()):
        print(key, ":", d[key])


    return d

def main():
    count_words('poem.txt')



if __name__ == '__main__':
    main()
    



'''
# Creating dataset
a = np.array([1,5,6,50,60,20])
 
# Creating histogram
fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(a, bins = [0, 25, 50, 75, 100])
 
# Show plot
plt.show()
'''