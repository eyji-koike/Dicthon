class Dictionary_API_Entry:
    '''
    Instantiate a Dictionary API entry. https://dictionaryapi.dev/
    This instance will query the entry on the API and enables you
    to access the following:
        ✔︎ Audio Pronunciation Links
        ✔︎ List of Antonyms
        ✔︎ List of Synonyms
        ✔︎ List of Word Classes
        ✔︎ List of Definitions
        ✔︎ List of Phonetic Text Representations
        ✔︎ Raw JSON entry



    '''

    def __init__(self, word):
        self.audio_links = []
        self.antonyms = []
        self.synonyms = []
        self.phonetic_texts = []
        self.phonetics = []
        self.definitions = []
        self.parts_of_speech = []
        self.meanings_list = []
        self.definitions_with_example = []
        self.word = word
        self.raw_entry = self.get_dict_entry()

    def get_dict_entry(self):
        import requests
        model_link = f'https://api.dictionaryapi.dev/api/v2/entries/en/{self.word}'
        entry = requests.get(model_link)
        self.raw_entry = entry.json()
        return self.raw_entry

    def get_all_meanings(self):
        for meanings in self.raw_entry[:]:
            if 'meanings' in meanings.keys():
                self.meanings_list.append(meanings['meanings'])
        return self.meanings_list

    def get_all_parts_of_speech(self):
        self.parts_of_speech = [partsOfSpeech[0]['partOfSpeech'] for partsOfSpeech in self.meanings_list[:]]
        return self.parts_of_speech

    def get_all_definitions(self):
        for definitions in self.meanings_list[:]:
            for definition in definitions[0]['definitions']:
                if 'definition' in definition.keys():
                    self.definitions.append(definition['definition'])
        return self.definitions

    def get_all_definitions_with_example(self):
        for definitions in self.meanings_list[:]:
            for definition in definitions[0]['definitions']:
                if 'example' in definition.keys():
                    self.definitions_with_example.append({'definition': definition['definition'],
                                                          'example': definition['example']})
        return self.definitions_with_example

    def get_all_phonetics(self):
        self.phonetics = [x['phonetics'] for x in self.raw_entry[:]]
        return self.phonetics

    def get_all_phonetic_texts(self):
        self.phonetic_texts = [[phonetic_text['text'] if 'text' in phonetic_text.keys() else None for
                                phonetic_text in phonetic[:]] for phonetic in self.phonetics[:]]
        return self.phonetic_texts

    def get_all_synonyms(self):
        self.synonyms = [[definitions['synonyms'] for definitions in
                          parts_of_speech] for parts_of_speech in self.meanings_list[:]]
        return self.synonyms

    def get_all_antonyms(self):
        self.antonyms = [[definitions['antonyms'] for definitions in
                          parts_of_speech] for parts_of_speech in self.meanings_list[:]]
        return self.antonyms

    def get_all_audio_links(self):
        self.audio_links = [
            [phonetics['audio'] if 'audio' in phonetics.keys() else None for phonetics in entry['phonetics']] for
            entry in self.raw_entry[:]]
        return self.audio_links
