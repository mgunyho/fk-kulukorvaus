import json

from weasyprint import HTML
from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@cross_origin()
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    # Read request data
    data = request.form.to_dict()

    # Generate pdf from html
    with open('out.html', 'w') as f:
        f.write(data['html'])
    HTML('out.html').write_pdf('out.pdf')

    # TODO: Use external service to send email

    return json.dumps(data)
