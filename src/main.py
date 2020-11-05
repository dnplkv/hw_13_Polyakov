from src.interface import Interface


def run():
    print("""This program can do following things with given .txt file. Select wanted operation:
    1. Takes a source text file and showing it.
    2. Conducts tokenization, lemmatization and stemming of a .txt file
    3. Removes stop words
    4. Returns the number of occurrences of each word in the .txt file
    5. Returns a given number of the most common words.
          """)
    while True:
        try:
            usr_input = int(input("Pick a wanted operation according to given list from 1 to 5: "))
            if 0 <= usr_input >= 6:
                raise Exception
        except:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    if usr_input == 1:
        Interface().First()
    if usr_input == 2:
        Interface().Second()
    if usr_input == 3:
        Interface().Third()
    if usr_input == 4:
        Interface().Fourth()
    if usr_input == 5:
        Interface().Fifth()

if __name__ == "__main__":
    run()
