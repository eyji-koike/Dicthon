class Dictionary_Entry:
    def __init__(self, word):
        self.definitions_list = []
        self.parts_of_speech_list = []
        self.meanings_list = []
        self.raw_entry = []
        self.word = word

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


if __name__ == '__main__':
    hello = Dictionary_Entry('pen')
    print(hello.raw_entry + hello.meanings_list)
    print(hello.get_all_meanings())
    print(hello.get_all_definitions())
    # hello_meanings = [y['meanings'] for y in hello[:]]
    # parts_of_speech = [x[0]['partOfSpeech'] for x in hello_meanings[:]]
    # definitions = [x[0]['definitions'][0]['definition'] for x in hello_meanings[:]]
    # print(len(hello))
    # print(hello_meanings)
    # pprint.pprint(definitions)
