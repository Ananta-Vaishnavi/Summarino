from flask import Flask, render_template, request
from summarize import generate_summary
from web_extract import extract_data_from_webpage

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/summarize', methods=['POST'])
def summarize():
    input_text = ''

    input_text = request.form['input_text']

    print("Input text:", input_text)  # Print the input text for debugging

    summary = generate_summary(input_text)

    return render_template("final.html", output=summary)


if __name__ == '__main__':
    app.run(debug=True)
