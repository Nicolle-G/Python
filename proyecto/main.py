def decorators(func):
    def result(word: str) -> bool:
        if func(word):
            print("The word is Palindrome")
            return True
        else:
            print("The word Not is a Palindrome")
            return False
    return result


@decorators
def is_palindrome(word: str) -> bool:
   invest = ""
   for i in reversed(word):
        invest += i
   return word == invest


def main():
    word = input("Give me a word:\n")
    is_palindrome(word)

