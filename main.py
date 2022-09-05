from Dicthon.dictionary_api_entry import Dictionary_API_Entry


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
    hello = Dictionary_API_Entry('cock')

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
    print(create_dict(hello.get_all_phonetic_texts()))
    print(hello.get_all_synonyms())
    print(hello.get_all_definitions_with_example())
    print(create_dict(hello.get_all_synonyms()))
    print(hello.__sizeof__())
