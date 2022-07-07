def language_input():
    """asks user to select a language"""
    english = "[1] English"
    spanish = "[2] Español"
    japanese = "[3] 日本語"
    while True:
        try:
            print(english + "\n" + spanish + "\n" + japanese + "")
            user_input = int(input("Please choose an option\n"))
            if user_input <= 0 or user_input > 3:
                print("Please choose a valid option:")
                continue
            return user_input
        except ValueError:
            print("Please enter a valid option: [1][2][3]")
            pass


def name_input(language):
    """asks user for their name, for nefarious purposes later"""
    selected_language = language
    if selected_language == 1:
        language_name = [language, input("What is your name?\n")]
        return language_name
    elif selected_language ==2:
        language_name = [language, input("¿Cuál es su nombre? (What is your name?)\n")]
        return language_name
    elif selected_language ==3:
        language_name = [language, input("o namae wa? (What is your name?)\n")]
        return language_name
    # greet(user_name)


def multilingual_greet(language_and_name):
    """prints a greeting to the given name" in specified language"""
    if language_and_name[0] == 1:
        print("Hey there " + language_and_name[1] + "!")
    elif language_and_name[0] == 2:
        print("Hola " + language_and_name[1] + "!")
    elif language_and_name[0] == 3:
        print("こんにちは " + language_and_name[1] + "-さん")


# print("greet docstring: " + multilingual_greet.__doc__)
# print("name input docstring: " + name_input.__doc__)

# name_input()
multilingual_greet(name_input(language_input()))
