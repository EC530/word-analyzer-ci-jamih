# word-analyzer-ci-jamih

# 

### Project Description
This project reads text from both a text file and PDF and displays a
histogram depicting the words detected and the frequency of those words
in the document. Words from NLTK's list of English stopwords are excluded
from the word count. In this project, the PDF and text files contain a verse 
from the poem "Stopping by Woods on a Snowy Evening" by Robert Frost.

### Work Phases
I divided my work flow into 3 phases.

Phase 1: Research and Initial Set Up
* Study GitHub Actions
* Define programming rules and styles
* Develop Github actions and implement rules using preferred linter (flake8)
* Develop the main console application or stub function

Phase 2: 
* Complete basic functionality of project
* Define unit tests using pytest for program and implement example 
 console application and one test


Phase 3:  Implementation and Testing
* Implement test programs and integrate them in GitHub actions
* Clean up code based on linter errors
* Modify pytests to increase coverage
* Complete and deliver project
 

### Project structure
The repo is as structured as follows:
/github -> /workflows -> /github-actions.yml
/pdf_analyzer.py: file for analyzing a PDF file
/poem.pdf
/poem.txt
/requirements.txt
/test_analyzer.py: pytest for testing both python programs
/word_analyzer.py: file for analyzing a text file


### Setup
To run this project, first clone the repo.

To run the text file word analyzer:
```
$ cd ../word-analyzer-ci-jamih
$ python word_analyzer.py
```

To run the PDF file word analyzer:
```
$ cd ../word-analyzer-ci-jamih
$ python pdf_analyzer.py
```






