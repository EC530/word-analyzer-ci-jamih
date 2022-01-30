import word_analyzer
import pdf_analyzer

dict = {'woods': 1, 'lovely': 1,
        'dark': 1, 'deep': 1, 
        'promises': 1, 'miles': 2, 'go': 2, 'sleep': 2}


def test_word_analyzer():
    '''word_analyzer should give known result with known input'''
    result = word_analyzer.txt_count_words('poem.txt')
    assert dict == result


def test_pdf_analyzer():
    '''pdf_analyzer should give known result with known input'''
    result = pdf_analyzer.pdf_count_words('poem.pdf')
    assert dict == result
