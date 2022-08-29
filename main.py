import pprint


def get_dict_entry(word):
    import requests
    modelLink = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    entry = requests.get(modelLink)
    return entry.json()


if __name__ == '__main__':
    hello = get_dict_entry('pen')
    hello_meanings = [y['meanings'] for y in hello[:]]
    parts_of_speech = [x[0]['partOfSpeech'] for x in hello_meanings[:]]
    definitions = [x[0]['definitions'] for x in hello_meanings[:]]
    print(len(hello))
    print(hello_meanings)
    pprint.pprint(definitions)
