# Lab 4 Report

<p>Author: Alexander Mulder<br>
Institution: Grand Valley State University <br>
Course and Section: CIS 343-01<p>

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
#### Test 1
```bash
python src/geco/geco.py ./test/lab4/"test1.txt"
```
#### Test 2
```bash
python src/geco/geco.py ./test/lab4/"test2.txt"
```
#### Test 3
```bash
python src/geco/geco.py ./test/lab4/"test3.txt"
```

## Test Cases

### Test 1
Output:
```bash
[línea 2] Error en 'cierto': Se espera ';' después del valor.
[línea 3] Error al final: Se esperaba una expresión.
```

### Test 2
Output:
```bash
one
True
3
nulo
None
```

### Test 3
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