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
        self.meanings_list = [meanings['meanings'] for meanings in self.raw_entry[:]]
        return self.meanings_list

    def get_all_parts_of_speech(self):
        self.parts_of_speech_list = [partsOfSpeech[0]['partOfSpeech'] for partsOfSpeech in self.meanings_list[:]]
        return self.parts_of_speech_list

    def get_all_definitions(self):
        self.definitions_list = [[definition['definition'] if 'definition' in definition.keys() else None for
                                  definition in definitions[0]['definitions']] for definitions in self.meanings_list[:]]
        return self.definitions_list

    def get_all_phonetics(self):
        self.phonetics_list = [x['phonetics'] for x in self.raw_entry[:]]
        return self.phonetics_list

    def get_all_phonetic_texts(self):
        self.phonetic_texts = [[phonetic_text['text'] if 'text' in phonetic_text.keys() else None for
                                phonetic_text in phonetic[:]] for phonetic in self.phonetics_list[:]]
        return self.phonetic_texts

    def get_all_synonyms(self):
        self.synonyms_list = [[definitions['synonyms'] for definitions in
                               parts_of_speech] for parts_of_speech in self.meanings_list[:]]
        return self.synonyms_list

    def get_all_antonyms(self):
        self.antonyms_list = [[definitions['antonyms'] for definitions in
                               parts_of_speech] for parts_of_speech in self.meanings_list[:]]
        return self.antonyms_list

    def get_all_audio_links(self):
        self.audio_links_list = [
            [phonetics['audio'] if 'audio' in phonetics.keys() else None for phonetics in entry['phonetics']] for
            entry in self.raw_entry[:]]
        return self.audio_links_list


def create_dict(listOfLists):
    new_list = []
    if type(listOfLists) == list:
        for list_item_first_level in listOfLists:
            if type(list_item_first_level) == list:
                for list_item_second_level in list_item_first_level:
                    if type(list_item_second_level) == list:
                        for list_item_third_level in list_item_second_level:
                            if type(list_item_third_level) == list:
                                print('list too deep, 4 levels')
                            else:
                                new_list.append(list_item_third_level)
                    else:
                        new_list.append(list_item_second_level)
            else:
                new_list.append(list_item_first_level)
    else:
        new_list = listOfLists

    return new_list


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
    pprint.pprint(create_dict(hello.get_all_synonyms()))
    print(hello.get_all_antonyms())
    print(hello.get_all_synonyms())
    print(hello.get_all_audio_links())
    print(create_dict(hello.get_all_synonyms()))
    print(hello.__sizeof__())

