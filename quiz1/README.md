# Calculator Expression Evaluator

This Python script demonstrates the use of ANTLR4 to parse and evaluate mathematical expressions. The implemented calculator can handle basic arithmetic operations, parentheses, and exponentiation.

## Usage

1. Install ANTLR4:

   ```bash
   pip install antlr4-python3-runtime
   ```

2. Generate lexer and parser:

   ```bash
   antlr4 -Dlanguage=Python3 Calculator.g4
   ```

3. Run the calculator:

   ```bash
   python calculator.py
   ```

## Example

### Input Expression

The input expression is specified in the `main` function of the `calculator.py` script. For example:

```python
input_expr = "(5-2)*2^2"
```

### Output

After running the script, the result of the expression will be printed:

```bash
Result of (5-2)*2^2 = 12.0
```

