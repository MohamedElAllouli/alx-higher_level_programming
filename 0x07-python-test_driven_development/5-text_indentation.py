#!/usr/bin/python3
def text_indentation(text):
    """
    adding 2 new lines after '.?:' chars.
    Args:
    text: The text.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for de in ".?:":
        text = (de + "\n\n").join(
                [line.strip(" ") for line in text.split(de)])
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
