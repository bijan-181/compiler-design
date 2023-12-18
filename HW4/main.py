from antlr4 import *
from gen.PasswordLexer import PasswordLexer
from gen.PasswordParser import PasswordParser


def validate_password(input_password):
    input_stream = InputStream(input_password)
    if input_stream.size < 8:
        return False
    lexer = PasswordLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PasswordParser(token_stream)
    tree = parser.password()
    if parser.getNumberOfSyntaxErrors() > 0:
        return False
    else:
        return True


# some test cases:
if __name__ == "__main__":
    passwords = ['asd123@#', 'sdda$$#@#@##@']
    checked_password = {
        "valid": [],
        "invalid": []
    }
    for password in passwords:

        if validate_password(password):
            checked_password["valid"].append(password)
        else:
            checked_password["invalid"].append(password)
