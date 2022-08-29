def get_dict_entry(word):
    import requests
    modelLink = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    entry = requests.get(modelLink)
    return entry.json()



if __name__ == '__main__':
    hello = get_dict_entry('hello')
    print(len(hello))
    print([x['partOfSpeech'] for x in hello[0]['meanings'][:]])
