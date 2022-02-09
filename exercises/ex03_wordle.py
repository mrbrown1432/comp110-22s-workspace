"""Ex03 - Structured Wordle."""

__author__ = "730481331"


def contains_char(word: str, character: str) -> bool:
    """Generates a bool that searches a string value for a certain character."""
    assert len(character) == 1
    instance_count: int = 0
    while instance_count != len(word):
        if character == word[instance_count]:
            return True
        instance_count += 1
    return False


white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Returns colored emoji boxes determined by if a character in the guess is in the secret."""
    assert len(guess) == len(secret)
    i: int = 0
    result: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            result = result + green_box
        elif contains_char(secret, guess[i]):
            result = result + yellow_box
        else: 
            result = result + white_box
        i = i + 1
    return result


def input_guess(number: int) -> str:
    """String to promt the user for a guess of an expected length."""
    word_length: str = input("Enter a " + f"{number}" + " character word: ")
    while len(word_length) != number:
        if len(word_length) != number:
            word_length = input("That wasn't " + f"{number}" + " chars! Try again: ")        
    return word_length


def main() -> None:
    """The entrypoint of the program and main game loop."""
    answer: str = "codes"
    g_string: str = ""
    turn_num: int = 0 
    while turn_num < len(answer):
        print(f"=== Turn {turn_num+1}/6 ===")
        g_string: str = input_guess(len(answer))
        emoji: str = emojified(g_string, answer)
        print(emoji)
        if g_string == answer:
            print(f"You won in {turn_num+1}/6 turns!")
            break
        turn_num += 1 
    if g_string > answer:
        print("x/6 - Sorry, try again tomorrow!")


if __name__ == "__main__": 
    main()