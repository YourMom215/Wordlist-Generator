from pathlib import Path
list_words = []
def create_letter_list():
    input_word = input("What chars do you want (no space in between) ")
    list_chars = [input_word[i] for i in range(len(input_word))]
    return(list_chars)
def create_wordlist(inputlist, iter_num,letter_list):
    current_list = []
    if len(inputlist) == 0:
        list_words.extend(letter_list)
        current_list.extend(letter_list)
    else:
        for word in inputlist:
            for letter in letter_list:
                list_words.append(word+letter)
                current_list.append(word+letter)
    if iter_num < len(letter_list)-1:
        create_wordlist(current_list, iter_num+1,letter_list)
    else:
        create_file(list_words)
def create_file(wordlist):
    file_path = Path.home() / "Downloads" / f"{input("Pick the name for your wordlist file ")}.txt"
    with file_path.open(mode="a") as file:
        for word in wordlist:
            file.write(f"{word}\n")
    print("Wordlist file is in downloads folder")
create_wordlist(list_words, 0,create_letter_list())
