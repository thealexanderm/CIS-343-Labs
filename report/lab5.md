# Lab 5 Report

<p>Author: Alexander Mulder<br>
Institution: Grand Valley State University <br>
Course and Section: CIS 343-01<p>

## Design Choices

### Variable Access Before Declaration
I chose the same design as Lox, so there will be a runtime error if a variable is accessed before declaration. This means that you can refer to a variable before it's declared, but you cannot evaluate it.

### Missing Initializer in the Declaration
Similar to Lox, if a variable isn't initialized in the declaration, then it will be set to None.

### Redeclaration
Like Lox, redeclaration of variables is supported and there is an error produced if an assignment target is invalid. Additionally, Geco implements a lexical scope.

## Setup Instructions

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

### Run Test Cases

#### Variable Declaration
```bash
python src/geco/geco.py ./test/lab5/"test-variable-declaration.txt"
```

#### Variable Access
```bash
python src/geco/geco.py ./test/lab5/"test-variable-access.txt"
```

#### Variable Assignment
```bash
python src/geco/geco.py ./test/lab5/"test-variable-assignment.txt"
```

#### Block Scope Test from the Textbook
```bash
python src/geco/geco.py ./test/lab4/"test3.txt"
```

#### Unmatched Braces in Blocks Error
```bash
python src/geco/geco.py ./test/lab5/"test-unmatched-braces-block-error.txt"
```

#### Invalid Assignment Targets Error
```bash
python src/geco/geco.py ./test/lab5/"test-invalid-assignment-targets-error.txt"
```

## Test Cases

### Variable Declaration
Output:
```bash
nulo
None
```

### Variable Access
Output:
```bash
this is a variable
None
```

### Variable Assignment
Output:
```bash
my variable assignment
None
```

### Block Scope from the Textbook
Output:
```bash
inner a
outer b 
global c
outer a
outer b
global c
global a
global b
global c
None
```
This code finds there nearest variable with the given identifier and prints that variable. The code begins in the innermost block where it prints a, b, and c. There is an "a" variable declared in that block with the value "inner a", so that is what is printed. Since there is no "b" variable in the innermost block, then it has to move out a level to find the "b" variable with the value "outer b". Since there is no "c" variable in that block, it needs to move out another level to find the "c" variable with the value "global c".

Next, since all the code in the innermost block has been executed, it moves to the next innermost block which prints variables a, b, and c again, except for this time we lose access to "a" variable in the innermost block, so we print "outer a", "outer b", and "global c". 

Finally, we move to the last block where we lose access to each of the deeper levels and print "global a", "global b", and "global c".

### Unmatched Braces in Blocks Error
Output:
```bash
[línea 19] Error al final: Se espera '}' después del bloque.
```

### Invalid Assignment Targets Error
Output:
```bash
Variable no definida 'a'. [línea 1]
None
```