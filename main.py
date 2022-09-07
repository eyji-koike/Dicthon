import pprint

from Dicthon import Dictionary_API_Entry


if __name__ == '__main__':
    hello = Dictionary_API_Entry('Hello')
    print(hello.get_all_synonyms())


