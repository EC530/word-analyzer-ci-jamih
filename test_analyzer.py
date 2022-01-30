import word_analyzer
import pdf_analyzer


dict = {'THE': 1, 'WOODS': 1, 'ARE': 1, 'LOVELY': 1, 'DARK': 1, 'AND': 3, 'DEEP': 1, 'BUT': 1, 'I': 3, 'HAVE': 1, 'PROMISES': 1, 'TO': 3, 'KEEP': 1, 'MILES': 2, 'GO': 2, 'BEFORE': 2, 'SLEEP': 2 }

def test_word_analyzer():
    '''word_analyzer should give known result with known input'''

    result = word_analyzer.txt_count_words('poem.txt')
    assert dict == result

def test_pdf_analyzer():
    '''word_analyzer should give known result with known input'''

    result = pdf_analyzer.pdf_count_words('poem.pdf')
    assert dict == result



