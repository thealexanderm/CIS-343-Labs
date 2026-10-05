
# Lab 1 Report

<p>Author: Alexander Mulder<br>
Institution: Grand Valley State University <br>
Course and Section: CIS 343-01<p>

## About Geco

### Language Name: Geco

### Regular Expressions

<p>Number Literals: <br>
String Literals:<br>
Identifiers: <p>

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
python3 src/geco/geco.py "ejémplo.txt"
```

### Interactive Mode
```bash
git clone "https://github.com/thealexanderm/CIS-343-LABS.git"
cd CIS-343-LABS
python3 src/geco/geco.py
```

### Tests
```bash
git clone "https://github.com/thealexanderm/CIS-343-LABS.git"
cd CIS-343-LABS
python3 test/lab1/test.py
```

## Test Cases

## Known Limitations
