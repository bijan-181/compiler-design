from antlr4 import *
from gen.EMailLexer import EMailLexer
from gen.EMailParser import EMailParser

def validate_email_address(email_address):
    # Create an ANTLR input stream from the input string
    input_stream = InputStream(email_address)

    # Create a lexer using the input stream
    lexer = EMailLexer(input_stream)

    # Create a token stream from the lexer
    token_stream = CommonTokenStream(lexer)

    # Create a parser from the token stream
    parser = EMailParser(token_stream)

    # Parse the input
    tree = parser.start()

    # Check if there are any syntax errors
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Invalid email address:", email_address)
    else:
        print("Valid email address:", email_address)

# Test with some sample email addresses
sample_emails = ["john.doe@example.com", "invalid.email@missingtoplevel", "user@inva!lid.com"]

for email in sample_emails:
    validate_email_address(email)
