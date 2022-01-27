f = open("sample.txt", "r")
#print(f.read())

# Create an empty dictionary
d = dict()
  
# Loop through each line of the file
for line in f:
    
  
    # Convert the characters in line to uppercase
    # to avoid case mismatch
    line = line.upper()

    # Remove the leading and trailing spaces
    line = line.strip()
  
    # Split the line into a list of words
    words = line.split(" ")
  
    # Iterate over each word in line
    for word in words:
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