import textwrap  # Módulo textwrap para manipular a indentação de strings


def print_recipe():
    recipe = """\
    1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
    2. Knead the dough for 10 minutes.
    3. Add 3g of Salt.
    4. Leave to rise for 2 hours.
    5. Bake at 200 degrees C for 30 minutes.
    """

    print(textwrap.dedent(recipe))


def print_modifiers():
    ###########################################################################
    # Basics:
    print("A 'single quote' inside a double quote")
    print('A "double quote" inside a single quote')
    print("Alternatively you can just \"escape\" the quote")
    print("You can even \\escape\\ the backslash")

    message = "Hello World!"
    print("With format string -> {} {}".format("hello", "friend"))
    print(f"With f-string -> {message}")
    print(r"With raw string -> C:\Users\Name\Document.txt")

    ###########################################################################
    # Unicode, Hexadecimal and Octal
    print("Unicode: \u00A9")
    print("Unicode with 32-bit hex value: \U0001F600")  # (Grinning face emoji)
    print("Unicode character by name: \N{LATIN SMALL LETTER E WITH ACUTE}")
    print("Hex: \x48\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64\x21")
    print("Octal: \110\145\154\154\157\040\127\157\162\154\144\041")
    ###########################################################################
    # Miscellaneous:
    print("First line\nSecond line")
    print("Column1\t\tColumn2")
    print("***This alert may emit a sound in the terminal***\a")
    # Erases the 'o', resulting in 'Hell World!'
    print("Backspace: Hello\b World!")
    # Moves to next page (new line in some terminals)
    print("Form feed (page break): Hello\fWorld!")
    # Carriage return: '<end>' overwrites 'Start', resulting in '<end> of line'
    print("Start of line\r<end>")
    # New line with vertical tab
    print("Vertical tab: Hello\vWorld!")


def main() -> None:
    print_recipe()
    print_modifiers()


if __name__ == '__main__':
    main()
