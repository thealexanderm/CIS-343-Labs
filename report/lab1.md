
# Lab 1 Report

<p>Author: Alexander Mulder<br>
Institution: Grand Valley State University <br>
Course and Section: CIS 343-01<p>

## About Geco

### Language Name: Geco

### Regular Expressions

<p>Number Literals: ^[0-9]+(,[0-9]+)?$<br>
String Literals: ^"[^"]*"$<br>
Identifiers: ^[^\W0-9]\w*$<p>

### Design Choices Relative to Lox

- My language is named "Geco" for two reasons. First, because it's short and easy to remember. Second, because I'd like to make a Spanish implementation of Lox for practice and since it's implemented in Python, I chose the name Geco because a gecko is another reptile and geco is the Spanish word for it.
- Many of my design choices spark from similar reasoning, for example, I chose to make my keywords/token-type-names the Spanish equivalents as well as the error messages.
- I didn't chose to make all of my function names Spanish because I was focused on what would be printed by the scanner in the terminal during usage.
- Many of the keyword names (such as "desde" and "sino") were inspired by the programming language [Latino](https://manual.lenguajelatino.org/en/latest/About-Latino.html) which is a programming language with Spanish syntax.
- I chose the function keyword "defi" as short for "definición" to be similar to Python function keyword "def" as short for "definition". I also implemented comments with "#" rather than "//" to be more similar to Python.
- The keywords I wasn't sure how to translate, I googled.
- I implemented the decimal point as a comma since that is common in Spain and many other Spanish-speaking countries.
- I also ensured that accented characters are considered in the allowed alphabet.
- Finally, I added the modulo operator as well the combination of assignment and operation in the "+=" or "-=" or equivalent because I like that feature and think it's handy.

## Dependency/Setup Instructions

### Source-file Mode
```bash
git clone "https://github.com/thealexanderm/CIS-343-LABS.git"
cd CIS-343-LABS
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/geco/geco.py "ejémplo.txt"
```

### Interactive Mode
```bash
git clone "https://github.com/thealexanderm/CIS-343-LABS.git"
cd CIS-343-LABS
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/geco/geco.py
```

### Tests
```bash
git clone "https://github.com/thealexanderm/CIS-343-LABS.git"
cd CIS-343-LABS
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest test/lab1
```

## Test Cases

### test_token_types

Purpose: to check if the tokens are being scanned as the correct token types

Input: [testtokens.txt](../test/lab1/testtokens.txt)

Expected Tokens/Errors:

```
(t.PAR_IZQ, "(", None),
(t.PAR_DER, ")", None),
(t.LLAVE_IZQ, "{", None),
(t.LLAVE_DER, "}", None),
(t.COMA, ",", None),
(t.PUNTO, ".", None),
(t.PUNTO_Y_COMA, ";", None),
(t.NEGACION, "!", None),
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
(t.CLASE, "clase", None),
(t.SINO, "sino", None),
(t.FALSO, "falso", None),
(t.DEFINICION, "defi", None),
(t.DESDE, "desde", None),
(t.SI, "si", None),
(t.NULO, "nulo", None),
(t.O, "o", None),
(t.IMPRIMIR, "imp", None),
(t.RETORNAR, "retorna", None),
(t.PADRE, "padre", None),
(t.ESTE, "este", None),
(t.CIERTO, "cierto", None),
(t.SEA, "sea", None),
(t.MIENTRAS, "mientras", None),
(t.FIN, "", None)
```
Output: [testtokensOUTPUT.txt](../test/lab1/testtokensOUTPUT.txt)

Matched expectations? Yes

### test_comma_decimal

Purpose: to check if the comma works as a decimal

Input: "3,14"

Expected Tokens/Errors:

```
(t.NUMERO, "3,14", 3.14),
(t.FIN, "", None)
```
Output:

```
Tipo.NUMERO 3,14 3.14
Tipo.FIN  None
```

Matched expectations? Yes

### test_number

Purpose: to check if non-decimal numbers are recognized

Input: "3"

Expected Tokens/Errors:

```
(t.NUMERO, "3", 3.0),
(t.FIN, "", None)
```
Output:

```
Tipo.NUMERO 3 3.0
Tipo.FIN  None
```

Matched expectations? Yes

### test_point_decimal

Purpose: to check that point decimal numbers are not recognized

Input: "3.14"

Expected Tokens/Errors:

```
(t.NUMERO, "3", 3.0),
(t.PUNTO, ".", None),
(t.NUMERO, "14", 14.0),
(t.FIN, "", None)
```
Output:

```
Tipo.NUMERO 3 3.0
Tipo.PUNTO . None
Tipo.NUMERO 14 14.0
Tipo.FIN  None
```

Matched expectations? Yes

### test_accents

Purpose: to check that accented characters are recognized

Input: "árbol público médico íntimo ratón año"

Expected Tokens/Errors:

```
(t.IDENTIFICADOR, "árbol", None),
(t.IDENTIFICADOR, "público", None),
(t.IDENTIFICADOR, "médico", None),
(t.IDENTIFICADOR, "íntimo", None),
(t.IDENTIFICADOR, "ratón", None),
(t.IDENTIFICADOR, "año", None),
(t.FIN, "", None)
```
Output:

```
Tipo.IDENTIFICADOR árbol None
Tipo.IDENTIFICADOR público None
Tipo.IDENTIFICADOR médico None
Tipo.IDENTIFICADOR íntimo None
Tipo.IDENTIFICADOR ratón None
Tipo.IDENTIFICADOR año None
Tipo.FIN  None
```

Matched expectations? Yes

### test_comments

Purpose: to check that comments are ignored

Input: '#this is a comment\n' \
        'sea a = "this is a string ####"'

Expected Tokens/Errors:

```
(t.SEA, "sea", None),
(t.IDENTIFICADOR, "a", None),
(t.ASIGNAR, "=", None),
(t.CADENA, '"this is a string ####"', 'this is a string ####'),
(t.FIN, "", None)
```
Output:

```
Tipo.SEA sea None
Tipo.IDENTIFICADOR a None
Tipo.ASIGNAR = None
Tipo.CADENA "this is a string ####" this is a string ####
Tipo.FIN  None
```

Matched expectations? Yes

### test_unexpected_character

Purpose: to check that there are errors for an unexpected character

Input: "@"

Expected Tokens/Errors: "[línea 1] Error: Carácter no esperado."

Output:

```
[línea 1] Error: Carácter no esperado.
Tipo.FIN  None
```

Matched expectations? Yes

### test_unterminated_string

Purpose: to check that there are errors for an unterminated string

Input: '"The neverending string....'

Expected Tokens/Errors: "[línea 1] Error: Cadena no cerrada."

Output:

```
[línea 1] Error: Cadena no cerrada.
Tipo.FIN  None
```

Matched expectations? Yes

### test_recovery

Purpose: to check that the scanner continues despite reporting errors

Input: ''$\n' \
        'sea a = 5\n' \
        '"The neverending string....'

Expected Tokens:

```
(t.SEA, "sea", None),
(t.IDENTIFICADOR, "a", None),
(t.ASIGNAR, "=", None),
(t.NUMERO, "5", 5.0),
(t.FIN, "", None)
```

Errors: "[línea 1] Error: Carácter no esperado."
        "[línea 3] Error: Cadena no cerrada."

Output:

```
[línea 1] Error: Carácter no esperado.
[línea 3] Error: Cadena no cerrada.
Tipo.SEA sea None
Tipo.IDENTIFICADOR a None
Tipo.ASIGNAR = None
Tipo.NUMERO 5 5.0
Tipo.FIN  None
```

Matched expectations? Yes

## Known Limitations
- Multi-line comments are not supported.
- Scientific number literals are not supported.
- String escape sequences are not supported.
- Error diagnostics are limited to the line number.
