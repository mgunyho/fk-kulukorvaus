# POC - Sähköinen Kulukorvauslomake

## Installation
Tested using Python 3.5

```
pip3 install weasyprint flask flask_cors
```

## Usage
```
export FLASK_APP=hello.py
flask run
```

Open `form.html` in browser, fill the form and submit and you should get `out.pdf` to your working directory.

## Pros & Cons
+ Easy to use
+ Supports complicated styling via CSS
+ Easy to maintain (updating form is done purely in html)
+ Relatively safe (only one minor security flaw in the pdf library that can be fixed if needed)