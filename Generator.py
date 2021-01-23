import random
from PyDictionary import PyDictionary

word_txt = open("words.txt", "r", encoding='utf8')
word_list = []
dict = PyDictionary()

char_to_replace = {'.': '',
                   ',': '',
                   ' ': ''}

def generator(letters):
    print(str(letters) + " letters. Let's go! \n")
    done = False
    try_count = 0

    while not done:
        try:
            random_word_string = word_list[random.randint(1,len(word_list))]
            for key, value in char_to_replace.items():
                random_word_string = random_word_string.replace(key, value)
                #print("Characters removed!"+ str(key) +"," +str(value))
            if len(random_word_string) == letters + 1:
                done = True
                print(random_word_string)
                try:
                    print("\n"+dict.meaning(random_word_string) + "\n")
                except:
                    print("\nNo Definition Found. \n-----------------------------")
            else:
                try_count += 1
                # print(str(try_count) +": Does not match. Finding new word. ")
        except:
            print("ERROR ERROR ERROR. \nPLEASE RETRY!\n\n")
            done = True

word_list = word_txt.readlines()
print(len(word_list))
random.shuffle(word_list)
word_txt.close()

while True:
    try:
        how_many_letters = int(input("How many letters in this randomly generated word? "))
        generator(how_many_letters)
    except ValueError:
        print("Sorry, please try that again.")