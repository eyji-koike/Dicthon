import unittest
from Dicthon import Dictionary_API_Entry


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.word = Dictionary_API_Entry('Hello')

    def test_raw_entry(self):
        answer = [{'word': 'hello', 'phonetics': [
            {'audio': 'https://api.dictionaryapi.dev/media/pronunciations/en/hello-au.mp3',
             'sourceUrl': 'https://commons.wikimedia.org/w/index.php?curid=75797336',
             'license': {'name': 'BY-SA 4.0', 'url': 'https://creativecommons.org/licenses/by-sa/4.0'}},
            {'text': '/həˈləʊ/', 'audio': 'https://api.dictionaryapi.dev/media/pronunciations/en/hello-uk.mp3',
             'sourceUrl': 'https://commons.wikimedia.org/w/index.php?curid=9021983',
             'license': {'name': 'BY 3.0 US', 'url': 'https://creativecommons.org/licenses/by/3.0/us'}},
            {'text': '/həˈloʊ/', 'audio': ''}], 'meanings': [{'partOfSpeech': 'noun', 'definitions': [
            {'definition': '"Hello!" or an equivalent greeting.', 'synonyms': [], 'antonyms': []}],
                                                              'synonyms': ['greeting'], 'antonyms': []},
                                                             {'partOfSpeech': 'verb', 'definitions': [
                                                                 {'definition': 'To greet with "hello".',
                                                                  'synonyms': [], 'antonyms': []}], 'synonyms': [],
                                                              'antonyms': []}, {'partOfSpeech': 'interjection',
                                                                                'definitions': [{
                                                                                    'definition': 'A greeting (salutation) said when meeting someone or acknowledging someone’s arrival or presence.',
                                                                                    'synonyms': [],
                                                                                    'antonyms': [],
                                                                                    'example': 'Hello, everyone.'},
                                                                                    {
                                                                                        'definition': 'A greeting used when answering the telephone.',
                                                                                        'synonyms': [],
                                                                                        'antonyms': [],
                                                                                        'example': 'Hello? How may I help you?'},
                                                                                    {
                                                                                        'definition': 'A call for response if it is not clear if anyone is present or listening, or if a telephone conversation may have been disconnected.',
                                                                                        'synonyms': [],
                                                                                        'antonyms': [],
                                                                                        'example': 'Hello? Is anyone there?'},
                                                                                    {
                                                                                        'definition': 'Used sarcastically to imply that the person addressed or referred to has done something the speaker or writer considers to be foolish.',
                                                                                        'synonyms': [],
                                                                                        'antonyms': [],
                                                                                        'example': 'You just tried to start your car with your cell phone. Hello?'},
                                                                                    {
                                                                                        'definition': 'An expression of puzzlement or discovery.',
                                                                                        'synonyms': [],
                                                                                        'antonyms': [],
                                                                                        'example': 'Hello! What’s going on here?'}],
                                                                                'synonyms': [],
                                                                                'antonyms': ['bye', 'goodbye']}],
                   'license': {'name': 'CC BY-SA 3.0', 'url': 'https://creativecommons.org/licenses/by-sa/3.0'},
                   'sourceUrls': ['https://en.wiktionary.org/wiki/hello']}]
        result = self.word.raw_entry
        self.assertEqual(result, answer)

    def test_get_all_meanings(self):
        answer = [[{'partOfSpeech': 'noun', 'definitions': [
            {'definition': '"Hello!" or an equivalent greeting.', 'synonyms': [], 'antonyms': []}],
                    'synonyms': ['greeting'], 'antonyms': []}, {'partOfSpeech': 'verb', 'definitions': [
            {'definition': 'To greet with "hello".', 'synonyms': [], 'antonyms': []}], 'synonyms': [], 'antonyms': []},
                   {'partOfSpeech': 'interjection', 'definitions': [{
                       'definition': 'A greeting (salutation) said when meeting someone or acknowledging someone’s arrival or presence.',
                       'synonyms': [], 'antonyms': [],
                       'example': 'Hello, everyone.'}, {
                       'definition': 'A greeting used when answering the telephone.',
                       'synonyms': [], 'antonyms': [],
                       'example': 'Hello? How may I help you?'}, {
                       'definition': 'A call for response if it is not clear if anyone is present or listening, or if a telephone conversation may have been disconnected.',
                       'synonyms': [], 'antonyms': [],
                       'example': 'Hello? Is anyone there?'}, {
                       'definition': 'Used sarcastically to imply that the person addressed or referred to has done something the speaker or writer considers to be foolish.',
                       'synonyms': [], 'antonyms': [],
                       'example': 'You just tried to start your car with your cell phone. Hello?'},
                       {
                           'definition': 'An expression of puzzlement or discovery.',
                           'synonyms': [], 'antonyms': [],
                           'example': 'Hello! What’s going on here?'}],
                    'synonyms': [], 'antonyms': ['bye', 'goodbye']}], [{'partOfSpeech': 'noun', 'definitions': [
            {'definition': '"Hello!" or an equivalent greeting.', 'synonyms': [], 'antonyms': []}],
                                                                        'synonyms': ['greeting'], 'antonyms': []},
                                                                       {'partOfSpeech': 'verb', 'definitions': [
                                                                           {'definition': 'To greet with "hello".',
                                                                            'synonyms': [], 'antonyms': []}],
                                                                        'synonyms': [], 'antonyms': []},
                                                                       {'partOfSpeech': 'interjection', 'definitions': [
                                                                           {
                                                                               'definition': 'A greeting (salutation) said when meeting someone or acknowledging someone’s arrival or presence.',
                                                                               'synonyms': [], 'antonyms': [],
                                                                               'example': 'Hello, everyone.'}, {
                                                                               'definition': 'A greeting used when answering the telephone.',
                                                                               'synonyms': [], 'antonyms': [],
                                                                               'example': 'Hello? How may I help you?'},
                                                                           {
                                                                               'definition': 'A call for response if it is not clear if anyone is present or listening, or if a telephone conversation may have been disconnected.',
                                                                               'synonyms': [], 'antonyms': [],
                                                                               'example': 'Hello? Is anyone there?'}, {
                                                                               'definition': 'Used sarcastically to imply that the person addressed or referred to has done something the speaker or writer considers to be foolish.',
                                                                               'synonyms': [], 'antonyms': [],
                                                                               'example': 'You just tried to start your car with your cell phone. Hello?'},
                                                                           {
                                                                               'definition': 'An expression of puzzlement or discovery.',
                                                                               'synonyms': [], 'antonyms': [],
                                                                               'example': 'Hello! What’s going on here?'}],
                                                                        'synonyms': [],
                                                                        'antonyms': ['bye', 'goodbye']}]]
        self.assertEqual(self.word.get_all_meanings(), answer)

    def test_get_all_parts_of_speech(self):
        answer = ['noun', 'verb', 'interjection']
        self.assertEqual(self.word.get_all_parts_of_speech(), answer)

    def test_get_all_definitions(self):
        answer = ['"Hello!" or an equivalent greeting.', 'To greet with "hello".',
                  'A greeting (salutation) said when meeting someone or acknowledging someone’s arrival or presence.',
                  'A greeting used when answering the telephone.',
                  'A call for response if it is not clear if anyone is present or listening, or if a telephone conversation may have been disconnected.',
                  'Used sarcastically to imply that the person addressed or referred to has done something the speaker or writer considers to be foolish.',
                  'An expression of puzzlement or discovery.']
        self.assertEqual(self.word.get_all_definitions(), answer)

    def test_get_all_definitions_with_example(self):
        answer = [{'definition': 'A greeting (salutation) said when meeting someone or acknowledging someone’s arrival or presence.', 'example': 'Hello, everyone.'}, {'definition': 'A greeting used when answering the telephone.', 'example': 'Hello? How may I help you?'}, {'definition': 'A call for response if it is not clear if anyone is present or listening, or if a telephone conversation may have been disconnected.', 'example': 'Hello? Is anyone there?'}, {'definition': 'Used sarcastically to imply that the person addressed or referred to has done something the speaker or writer considers to be foolish.', 'example': 'You just tried to start your car with your cell phone. Hello?'}, {'definition': 'An expression of puzzlement or discovery.', 'example': 'Hello! What’s going on here?'}, {'definition': 'A greeting (salutation) said when meeting someone or acknowledging someone’s arrival or presence.', 'example': 'Hello, everyone.'}, {'definition': 'A greeting used when answering the telephone.', 'example': 'Hello? How may I help you?'}, {'definition': 'A call for response if it is not clear if anyone is present or listening, or if a telephone conversation may have been disconnected.', 'example': 'Hello? Is anyone there?'}, {'definition': 'Used sarcastically to imply that the person addressed or referred to has done something the speaker or writer considers to be foolish.', 'example': 'You just tried to start your car with your cell phone. Hello?'}, {'definition': 'An expression of puzzlement or discovery.', 'example': 'Hello! What’s going on here?'}]
        self.assertEqual(self.word.get_all_definitions_with_example(), answer)

    def test_get_all_phonetics(self):
        answer = [[{'audio': 'https://api.dictionaryapi.dev/media/pronunciations/en/hello-au.mp3',
                    'sourceUrl': 'https://commons.wikimedia.org/w/index.php?curid=75797336',
                    'license': {'name': 'BY-SA 4.0', 'url': 'https://creativecommons.org/licenses/by-sa/4.0'}},
                   {'text': '/həˈləʊ/', 'audio': 'https://api.dictionaryapi.dev/media/pronunciations/en/hello-uk.mp3',
                    'sourceUrl': 'https://commons.wikimedia.org/w/index.php?curid=9021983',
                    'license': {'name': 'BY 3.0 US', 'url': 'https://creativecommons.org/licenses/by/3.0/us'}},
                   {'text': '/həˈloʊ/', 'audio': ''}],
                  [{'audio': 'https://api.dictionaryapi.dev/media/pronunciations/en/hello-au.mp3',
                    'sourceUrl': 'https://commons.wikimedia.org/w/index.php?curid=75797336',
                    'license': {'name': 'BY-SA 4.0', 'url': 'https://creativecommons.org/licenses/by-sa/4.0'}},
                   {'text': '/həˈləʊ/', 'audio': 'https://api.dictionaryapi.dev/media/pronunciations/en/hello-uk.mp3',
                    'sourceUrl': 'https://commons.wikimedia.org/w/index.php?curid=9021983', 'license':
                        {'name': 'BY 3.0 US', 'url': 'https://creativecommons.org/licenses/by/3.0/us'}},
                   {'text': '/həˈloʊ/', 'audio': ''}]]
        self.assertEqual(self.word.get_all_phonetics(), answer)

    def test_get_all_phonetic_text_representations(self):
        answer = ['/həˈləʊ/', '/həˈloʊ/']
        self.assertEqual(self.word.get_all_phonetic_text_representation(), answer)

    def test_get_all_synonyms(self):
        answer = [['greeting']]
        self.assertEqual(self.word.get_all_synonyms(), answer)

    def test_get_all_antonyms(self):
        answer = [['bye', 'goodbye']]
        self.assertEqual(self.word.get_all_antonyms(), answer)

    def test_get_all_audio_links(self):
        answer = ['https://api.dictionaryapi.dev/media/pronunciations/en/hello-au.mp3', 'https://api.dictionaryapi.dev/media/pronunciations/en/hello-uk.mp3']
        self.assertEqual(self.word.get_all_audio_links(), answer)


if __name__ == '__main__':
    unittest.main()
