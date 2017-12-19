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