# Password Validator

## Overview

This project provides a simple password validation tool implemented in Python using the ANTLR4 library. The tool checks if a given password meets certain criteria specified by the provided grammar.

## Grammar

The password validation grammar includes the following rules:

- `password`: Defines valid password patterns with combinations of characters (`CHARS`), digits (`DIGITS`), and special characters (`SPECIALCHARS`).

- `CHARS`: Represents alphabetical characters (both lowercase and uppercase).

- `DIGITS`: Represents numeric digits.

- `SPECIALCHARS`: Represents special characters often used in passwords.

## How to Use

1. Install the required dependencies:

   ```bash
   pip install antlr4-python3-runtime
   ```

2. Run the `validate_password` function in the `main.py` file by passing a password string to it. The function returns `True` if the password is valid according to the defined grammar, and `False` otherwise.

   ```python
   from main import validate_password

   password = "your_password_here"

   if validate_password(password):
       print("Password is valid!")
   else:
       print("Password is invalid.")
   ```

## Example

```python
from main import validate_password

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

print("Valid passwords:", checked_password["valid"])
print("Invalid passwords:", checked_password["invalid"])
```

## Notes

- The minimum password length is set to 8 characters.

- Feel free to customize the grammar rules in the `Password.g4` file based on your specific requirements.