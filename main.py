def decorators(func):
    def result(word: str) -> str:
        if func(word):
            print("The word is Palindrome")
        else:
            print("The word Not is a Palindrome")
    return result


@decorators
def is_palindrome(word: str) -> str:
   invest = ""
   for i in reversed(word):
        invest += i
   return word == invest


def main():
    word = input("Give me a word:\n")
    is_palindrome(word)



