dictionary_save = {
    "clothing": 1,
    "hair": 1,
    "shoes": 1,
    "makeup": 1,
    "accessories": 1,
    "eyecolors": 1,
    "skintones": 1,
}


def dictionary_change():
    file = open("page.txt", "r+")
    reader = file.readlines()
    file.close()
    for key, value in dictionary_save.items():
        dictionary_save[key] = int(reader[reader.index(key + '\n')+1])


def overwrite(val, search_type):
    dictionary_change()
    file = open("page.txt", "w+")
    dictionary_save[search_type] = val
    for key, value in dictionary_save.items():
        file.write('%s\n%d\n' % (key, value))
    file.close()


def range_base(search_type):
    file = open("page.txt", "r+")
    reader = file.readlines()
    file.close()
    return int(reader[reader.index(search_type + '\n')+1])


def search_for(search_type):
    file = open("piece.txt", "r+")
    reader = file.readlines()
    file.close()
    return reader[reader.index(search_type + '\n')+1].rstrip()


def set_up():
    file = open("page.txt", "w+")
    for key, value in dictionary_save.items():
        file.write('%s\n%d\n' % (key, value))
    file.close()
