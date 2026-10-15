# Lab 2 Report

<p>Author: Alexander Mulder<br>
Institution: Grand Valley State University <br>
Course and Section: CIS 343-01<p>

## Geco Grammar

### Supported Operators and Literal Types

My printer supports every operator and literal listed in [token_type.py](../src/geco/token_type.py). The grammar that is supported includes Expression, Binary, Unary, Grouping, and Literal, which was implemented as implemented in Lox.

### Design Choices Relative to Lox

My design choices are practically equivalent to those for Lox's grammar. I did not use meta-programming to create my AST Printer. My printer is capable of printing my Token additions from Lab 1.

## Setup Instructions

### Run Built-In Example
```bash
git clone "https://github.com/thealexanderm/CIS-343-LABS.git"
cd CIS-343-LABS
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/geco/ast_printer
```

### Run Test Cases
```bash
git clone "https://github.com/thealexanderm/CIS-343-LABS.git"
cd CIS-343-LABS
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest test/lab2/printer_test.py
```

## Test Cases

### testExprDefault

Purpose: to test the default expression as given in the main function of the AST printer and in the Crafting Interpreters book.

Hard-coded AST:
```python
Binary(
    Unary(
        Token(t.MENOS, "-", None, 1),
        Literal(123)),
    Token(t.ESTRELLA, "*", None, 1),
    Grouping(
        Literal(45.67)))
```

Expected Output:
```python
(* (- 123) (group 45.67))
```

Actual Printer Output:
```bash
(* (- 123) (group 45.67))
```

Matched expectations? Yes

### testOperators

Purpose: to test if each operator is able to be included as an operator in a Binary expression.

Hard-coded AST:
```python
operators = [
    (t.NO_IGUAL, "!=", None),
    (t.MAYOR, ">", None),
    (t.MAYOR_IGUAL, ">=", None),
    (t.MENOR, "<", None),
    (t.MENOR_IGUAL, "<=", None),
    (t.MENOS, "-", None),
    (t.MENOS_ASIGNAR, "-=", None),
    (t.MODULO, "%", None),
    (t.MODULO_ASIGNAR, "%=", None),
    (t.MAS, "+", None),
    (t.MAS_ASIGNAR, "+=", None),
    (t.BARRA, "/", None),
    (t.DIV_ASIGNAR, "/=", None),
    (t.ESTRELLA, "*", None),
    (t.ESTRELLA_ASIGNAR, "*=", None),
    (t.ASIGNAR, "=", None),
    (t.IGUAL_IGUAL, "==", None),
    (t.Y, "y", None),
    (t.O, "o", None)
]

for tipo, lexema, literal in operators:
    expression = Binary(
        Literal(1),
        Token(tipo, lexema, None, 1),
        Literal(2))
```

Expected Output:
```python
({lexema} 1 2)
```

Actual Printer Output:
```bash
(!= 1 2)
(> 1 2)
(>= 1 2)
(< 1 2)
(<= 1 2)
(- 1 2)
(-= 1 2)
(% 1 2)
(%= 1 2)
(+ 1 2)
(+= 1 2)
(/ 1 2)
(/= 1 2)
(* 1 2)
(*= 1 2)
(= 1 2)
(== 1 2)
(y 1 2)
(o 1 2)
```

Matched expectations? Yes

### testUnaryNegation

Purpose: to test the negation operator in Unary expression.

Hard-coded AST:
```python
Unary(
    Token(t.NEGACION, "!", None, 1),
    Literal(5)
)
```

Expected Output:
```python
(! 5)
```

Actual Printer Output:
```bash
(! 5)
```

Matched expectations? Yes

### testNestedUnary

Purpose: to test that Unarys may be nested.

Hard-coded AST:
```python
Unary(
    Token(t.MENOS, "-", None, 1),
    Unary(
        Token(t.MENOS, "-", None, 1),
        Literal(1)
    ))
```

Expected Output:
```python
(- (- 1))
```

Actual Printer Output:
```bash
(- (- 1))
```

Matched expectations? Yes

### testNestedGrouping

Purpose: to test that Groupings may be nested.

Hard-coded AST:
```python
Grouping(
    Grouping(
        Literal(1)
    )
)
```

Expected Output:
```python
(group (group 1))
```

Actual Printer Output:
```bash
(group (group 1))
```

Matched expectations? Yes

### testString

Purpose: to test that String literals print properly.

Hard-coded AST:
```python
Literal("hola")
```

Expected Output:
```python
hola
```

Actual Printer Output:
```bash
hola
```

Matched expectations? Yes

## Known Limitations
- Pylance import errors have been suppressed.