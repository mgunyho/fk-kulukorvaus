import json

from weasyprint import HTML
from bs4 import BeautifulSoup
from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

html_template = """
<html>
  <head>
    <title>kulukorvauslomake</title>
  </head>
  <body>
  </body>
</html>
"""

@cross_origin()
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    # Read request data
    data = request.form.to_dict()

    soup = BeautifulSoup(html_template, "html.parser")

    # append data to html template
    # TODO: get keys from template instead of iterating through all of them
    # TODO: sanitize input
    for key, val in data.items():
      tag = soup.new_tag("p", style="font-family: sans-serif")
      tag.string = "{}: {}".format(key, val)
      soup.body.append(tag)
      print(tag)

    # generate pdf
    HTML(string = str(soup)).write_pdf('out.pdf')

    # TODO: Use external service to send email

    return json.dumps(data)
