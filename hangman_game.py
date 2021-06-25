import random
import os

def hangman_game():
    print("====================================================================================================")
    print("██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗  ░██████╗░░█████╗░███╗░░░███╗███████╗")
    print("██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║  ██╔════╝░██╔══██╗████╗░████║██╔════╝")
    print("███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║  ██║░░██╗░███████║██╔████╔██║█████╗░░")
    print("██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░")
    print("██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗")
    print("╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝")
    print("====================================================================================================")


def control_board(attemps, words_guessed):
    print(f"Attemps left: {attemps}\t\tWords guessed: {words_guessed}")

    
def compare_words(complete_word, guessed_letters):
    guessed = [" " for i in range(len(complete_word))]
    guessed_letters = list(set(guessed_letters))

    # Complete the word's letters guessed in the game 
    for i in range(len(guessed_letters)):
        for j in range(len(complete_word)):
            if guessed_letters[i] == complete_word[j]:
                guessed[j] = guessed_letters[i]

    return guessed


def remove_accents(word):
    replacements = (
        ("Á", "A"),
        ("É", "E"),
        ("Í", "I"),
        ("Ó", "O"),
        ("Ú", "U"),
    )
    for a, b in replacements:
        word = word.replace(a, b)
    return word


def read_file(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            # Remove blanck spaces in the strings
            words = [word.strip() for word in f]
        return words
    except FileNotFoundError:
        return []


def main():
    game_over = False

    words = read_file("./files/words.txt")
    assert len(words) != 0, "The game can't start. There are not words in the game."

    word_game = remove_accents(words[random.randint(0, len(words)-1)].upper())
    word_list = [word_game[i] for i in range(len(word_game))]
    letters_user = []
    guessed = []
    attemps = 0
    words_guessed = 0
    max_attemps = 20
    os.system("cls")

    while not(game_over or attemps > max_attemps):
        
        os.system("cls")
        hangman_game()
        control_board(max_attemps-attemps, words_guessed)

        for i in range(len(guessed)):
            print('{} '.format(guessed[i]), end="")
        print() 
        for i in range(len(word_list)):
            print('_ ', end="")
        print()
        
        attemps = attemps + 1

        letter = input("Type a letter: ").upper()

        while len(letter) != 1 or str.isdigit(letter):
            letter = input("Don't type numbers, symbols or words. Type a letter: ").upper()

        letters_user.append(letter)

        guessed = compare_words(word_list, letters_user)

        if word_game == "".join(guessed):
            words_guessed = words_guessed + 1
            word_game = remove_accents(words[random.randint(0, len(words)-1)].upper())
            word_list = [word_game[i] for i in range(len(word_game))]
            letters_user = []

            # Increase the game's difficult
            if words_guessed <= 3:
                max_attemps = 20
            elif 3 < words_guessed <= 6:
                max_attemps = 15
            elif words_guessed > 6:
                max_attemps = 10
            
            attemps = 0
            guessed = []
        
        if attemps > max_attemps:
            game_over = True
            print("The correct word is: ", word_game)
        
        
    print("█▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█")
    print("█▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄")

         
if __name__ == "__main__":
    main()