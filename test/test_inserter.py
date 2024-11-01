from src._text_inserter import text_insterer


if __name__ == "__main__":
    test_text = '<span style="style";">1234</span><span style="style">5678</span>'

    for i in range(20 + 1):
        print(text_insterer(test_text, i, "[===]", debug=True))

    # insert empty string test
    for i in range(20 + 1):
        print(text_insterer(test_text, i, "", debug=True))

    # insert empty string to shrot string # 不会发生
    for i in range(20 + 1):
        print(text_insterer("1", i, "", debug=True))

    # insert empty string to empty string
    for i in range(20 + 1):
        print(text_insterer("", i, "", debug=True))

    # insert string to empty string
    for i in range(20 + 1):
        print(text_insterer("", i, "123", debug=True))
