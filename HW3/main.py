from antlr4 import *
from gen.ExtractInfoLexer import ExtractInfoLexer
from gen.ExtractInfoParser import ExtractInfoParser


def validate_iranian_national_id(national_id):
    total = 0
    for i in range(9):
        digit = int(national_id[i])
        total += digit * (10 - i)

    last_digit = int(national_id[9])
    remainder = total % 11

    return (2 > remainder == last_digit) or (remainder >= 2 and last_digit == 11 - remainder)


def main(input_string):
    tokens = {
        "URL": [],
        "EMail": [],
        "National Code": [],
        "Postal Code": [],
        "Phone": [],
        "Float": [],
        "NotMach": [],
    }
    input_stream = InputStream(input_string)
    lexer = ExtractInfoLexer(input_stream)
    for token in lexer.getAllTokens():
        if token.type == 1:
            tokens["URL"].append(token.text)
            # print("Found URL:", token.text)
        if token.type == 2:
            tokens["EMail"].append(token.text)
            # print("Found EMail:", token.text)
        elif token.type == 3:
            if validate_iranian_national_id(token.text):
                tokens["National Code"].append(token.text)
                # print("Found National Code:", token.text)
            else:
                tokens["Postal Code"].append(token.text)
                # print("Found Postal Code:", token.text)
        elif token.type == 4:
            tokens["Phone"].append(token.text)
            # print("Found Phone Number:", token.text)
        elif token.type == 5:
            tokens["Float"].append(token.text)
            # print("Found Float:", token.text)
        elif token.type == 6:
            tokens["NotMach"].append(token.text)
            # print("NotMach:", token.text)
    for i, j in tokens.items():
        print(i, ":", j)


if __name__ == "__main__":
    string = """http://example.com/subpath https://www.google.com/search
2027041710 
09112583697 485.36
some2random@mail.com 8189526871
4589.368 here we have text
548.69
1589325697
some randome text 
"""  # Replace with your actual input string
    main(string)
