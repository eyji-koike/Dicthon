import pprint

from Dicthon import Dictionary_API_Entry


if __name__ == '__main__':
    hello = Dictionary_API_Entry('dog')
    hello.get_dict_entry()
    print(hello.raw_entry)
    print('meanings: ')
    pprint.pprint(hello.get_all_meanings())
    print('phonetics: ')
    print(hello.get_all_phonetics())
    print('entry: ')
    print(hello.get_dict_entry())
    print('definitions: ')
    print(hello.get_all_definitions())
    print('parts of speech: ')
    print(hello.get_all_parts_of_speech())
    print('phonetic texts: ')
    print(hello.get_all_phonetic_text_representation())
    print(hello.get_all_synonyms())
    print(hello.get_all_antonyms())
    print(hello.get_all_definitions_with_example())
    print(hello.get_all_audio_links())
    print(hello.__sizeof__())
