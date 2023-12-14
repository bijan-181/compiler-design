# ExtractInfo-ANTLR-Python

This repository provides an ANTLR grammar file [(`ExtractInfo.g4`)](gen/ExtractInfo.g4) designed to extract
information such as URLs,
email addresses, Iranian national codes, phone numbers, floats, and more from a given text. Additionally, it includes a
Python script [(`main.py`)](main.py) that utilizes the generated lexer and parser to tokenize and categorize input text.

## ANTLR Grammar

### ExtractInfo.g4

The [`ExtractInfo.g4`](gen/ExtractInfo.g4) file contains the ANTLR4 grammar for recognizing various patterns in text. The grammar defines
rules for matching and extracting different types of information, including:

- **URLs**: Recognizes both HTTP and HTTPS URLs, including optional "www" subdomains and various path components.
- **Email addresses**: Matches standard email addresses with local and domain parts.
- **Iranian national codes**: Validates Iranian national identification numbers using a custom validation function.
- **Postal Code**: Matches 10-digit postal codes.
- **Phone numbers**: Identifies 11-digit phone numbers.
- **Floats**: Matches decimal numbers.
- **Words**: Catches alphanumeric characters, hyphens, and selected symbols.
- **WS**: Skips whitespace characters.

Feel free to modify the grammar to suit your specific use case or extend it to recognize additional patterns.

## Python Script

### main.py

The [`main.py`](main.py) script serves as an example of how to use the generated lexer and parser from the ANTLR grammar. It
tokenizes the input text and categorizes the extracted tokens into different types, such as URLs, email addresses,
national codes, phone numbers, floats, and unmatched text.

#### Usage

1. Ensure you have Python 3.x installed.

2. Install the required Python packages:

   ```bash
   pip install antlr4-python3-runtime
   ```

3. Run the script:

   ```bash
   python main.py
   ```

   Replace the sample input in the script with your actual text to see the tokenization results.
