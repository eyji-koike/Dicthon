import pprint


class Dictionary_Entry:
    def __init__(self, word):
        self.audio_links_list = []
        self.antonyms_list = []
        self.synonyms_list = []
        self.phonetic_texts = []
        self.phonetics_list = []
        self.definitions_list = []
        self.parts_of_speech_list = []
        self.meanings_list = []
        self.word = word
        self.raw_entry = self.get_dict_entry()

    def get_dict_entry(self):
        import requests
        model_link = f'https://api.dictionaryapi.dev/api/v2/entries/en/{self.word}'
        entry = requests.get(model_link)
        self.raw_entry = entry.json()
        return entry.json()

    def get_all_meanings(self):
        self.meanings_list = [x['meanings'] for x in self.raw_entry[:]]
        return [x['meanings'] for x in self.raw_entry[:]]

    def get_all_parts_of_speech(self):
        self.parts_of_speech_list = [x[0]['partOfSpeech'] for x in self.meanings_list[:]]
        return [x[0]['partOfSpeech'] for x in self.meanings_list[:]]

    def get_all_definitions(self):
        self.definitions_list = [x[0]['definitions'][0]['definition'] for x in self.meanings_list[:]]
        return [x[0]['definitions'][0]['definition'] for x in self.meanings_list[:]]

    def get_all_phonetics(self):
        self.phonetics_list = [x['phonetics'] for x in self.raw_entry[:]]
        return [x['phonetics'] for x in self.raw_entry[:]]

    def get_all_phonetic_texts(self):
        self.phonetic_texts = [[y['text'] if 'text' in y.keys() else None for y in x[:]] for x in
                               self.phonetics_list[:]]
        return [[y['text'] if 'text' in y.keys() else None for y in x[:]] for x in self.phonetics_list[:]]

    def get_all_synonyms(self):
        self.synonyms_list = [[definitions['synonyms'] for definitions in
                               parts_of_speech] for parts_of_speech in self.meanings_list[:]]
        return [[definitions['synonyms'] for definitions in
                 parts_of_speech] for parts_of_speech in self.meanings_list[:]]

    def get_all_antonyms(self):
        self.antonyms_list = [[definitions['antonyms'] for definitions in
                               parts_of_speech] for parts_of_speech in self.meanings_list[:]]
        return [[definitions['antonyms'] for definitions in
                 parts_of_speech] for parts_of_speech in self.meanings_list[:]]

    def get_all_audio_links(self):
        self.audio_links_list = [
            [phonetics['audio'] if 'audio' in phonetics.keys() else None for phonetics in entry['phonetics']] for
            entry in self.raw_entry[:]]
        return [[phonetics['audio'] if 'audio' in phonetics.keys() else None for phonetics in entry['phonetics']] for
                entry in self.raw_entry[:]]


if __name__ == '__main__':
    hello = Dictionary_Entry('cock')

    print(hello.raw_entry)
    print('meanings: ')
    print(hello.get_all_meanings())
    print('phonetics: ')
    print(hello.get_all_phonetics())
    print('entry: ')
    print(hello.get_dict_entry())
    print('definitions: ')
    print(hello.get_all_definitions())
    print('parts of speech: ')
    print(hello.get_all_parts_of_speech())
    print('phonetic texts: ')
    pprint.pprint(hello.get_all_phonetic_texts())
    print(hello.get_all_synonyms())
    print(hello.get_all_antonyms())
    print(hello.get_all_audio_links())
    print(hello.__sizeof__())
    # hello_meanings = [y['meanings'] for y in hello[:]]
    # parts_of_speech = [x[0]['partOfSpeech'] for x in hello_meanings[:]]
    # definitions = [x[0]['definitions'][0]['definition'] for x in hello_meanings[:]]
    # print(len(hello))
    # print(hello_meanings)
    # pprint.pprint(definitions)
