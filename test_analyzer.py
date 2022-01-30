import word_analyzer
import pdf_analyzer

dict = {'woods': 1, 'lovely': 1,
        'dark': 1, 'deep': 1, 'promises': 1,
        'keep': 1, 'miles': 2, 'go': 2, 'sleep': 2}

w = {'woods', 'lovely', 'dark', 'deep', 'promises',
     'keep', 'miles', 'go', 'sleep'}
f = {1, 1, 1, 1, 1, 2, 2, 2}


def test_word_analyzer():
    '''word_analyzer should give known result with known input'''
    result = word_analyzer.txt_count_words('poem.txt')
    words, freq = word_analyzer.txt_histogram(result)
    assert dict == result and w == words and f == freq
    


def test_pdf_analyzer():
    '''pdf_analyzer should give known result with known input'''
    result = pdf_analyzer.pdf_count_words('poem.pdf')
    words, freq = word_analyzer.txt_histogram(result)
    assert dict == result and w == words and f == freq
