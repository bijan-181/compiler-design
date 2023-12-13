# Email Address ANTLR Grammar

This repository contains an ANTLR grammar for parsing email addresses. The grammar defines the structure of a valid email address and can be used to generate lexer and parser files for various programming languages, including Python.

## Grammar Definition

The grammar is defined in the `EMail.g4` file. It consists of two main rules:

- `LOCAL_SUBPART`: Represents the local part of the email address and allows a variety of characters commonly found in email local parts.
- `DOMAIN_SUBPART`: Represents the domain part of the email address and allows alphanumeric characters and hyphens.

The main rule `EMAIL` combines these subparts to define a valid email address format.


## Generating Lexer and Parser Files

To generate the lexer and parser files for your preferred programming language (e.g., Python), you can use the ANTLR4 tool. Install ANTLR4 and run the following command:

```bash
antlr4 -Dlanguage=Python3 EMail.g4
```

This will generate the lexer (`EMailLexer.py`) and parser (`EMailParser.py`) files.

## Using the Generated Files in Python

Now that you have the lexer and parser files, you can use them in your Python code to parse email addresses. Here's a simple example:
[main.py](main.py)

input :
```
john.doe@example.com
invalid.email@missingtoplevel
user@inva!lid.com
```
output :
```
Valid email address: john.doe@example.com
Invalid email address: invalid.email@missingtoplevel
Invalid email address: user@inva!lid.com
```