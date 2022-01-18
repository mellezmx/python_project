
import getpass
import random


def main():



    print('-------------------- WELCOME TO HANGMAN ---------------------')

    #def ask_for_word():

        #return getpass.getpass("Enter your value and let's the fun begin: ")
        #return getpass.win_getpass("Enter your value and let's the fun begin: ")

    def random_word_choice():
        print("A word have been randomly chosen. Let's start.")
        return random.choice(open("word.txt").read().split())

    def display_word(secret_word, good_letters):
        for l in secret_word:
            if l in good_letters:
                print(l, end='')
            else:
                print('-', end='')

    def end_game(secret_word, good_letters):
        for letter in secret_word:
            if letter in good_letters:
                continue
            else:
                return False
        print('You found the secret word %s. Congrats' %secret_word)
        return True


    def choice_of_letter(secret_word, good_letters, bad_letters):
        flag = False
        while(True):
            letter = input("      Pick a letter... :  ")
            if letter in good_letters or letter in bad_letters:
                print('\nYou already choose this letter. Choose another one...')
            elif letter in secret_word:
                good_letters.append(letter)
                flag = True
                if end_game(secret_word, good_letters):
                    return exit()
                print('Great!')
                break
            else:
                print('Sorry, wrong choice')
                bad_letters.append(letter)
                break
        return flag

    def the_game():
        good_letters = []
        bad_letters = []
        number_of_try = 10

        secret_word = random_word_choice()

        for _ in secret_word:
            print('-', end='')

        while(number_of_try > 0):
            print('You have %s try left' % number_of_try)
            flag = choice_of_letter(secret_word, good_letters, bad_letters)
            display_word(secret_word, good_letters)
            if not flag:
                number_of_try-=1
        if number_of_try == 0:
            print('\nYou loose :(')




    the_game()


if __name__ == '__main__':
    main()
