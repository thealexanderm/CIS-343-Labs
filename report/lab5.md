# Lab 5 Report

<p>Author: Alexander Mulder<br>
Institution: Grand Valley State University <br>
Course and Section: CIS 343-01<p>

## Design Choices

### Variable Access Before Declaration

### Missing Initializer in the Declaration

### Redeclaration

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

#### Variable Access

#### Variable Assignment

#### Block Scope Test from the Textbook
```bash
python src/geco/geco.py ./test/lab4/"test3.txt"
```

#### Unmatched Braces in Blocks Error

#### Invalid Assignment Targets Error

## Test Cases

### Variable Declaration

### Variable Access

### Variable Assignment

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

### Unmatched Braces in Blocks Error

### Invalid Assignment Targets Error
