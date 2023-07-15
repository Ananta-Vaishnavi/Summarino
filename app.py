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

    if request.form.get('article-url'):
        # If URL field is filled, use its value
        input_text = request.form['article-url']
    elif request.form.get('article-text'):
        # Otherwise, use the value from the textarea
        input_text = request.form['article-text']

    # Perform any required operations with the input text
    # For example, pass it to the summarization function
    summary = generate_summary(input_text)

    return render_template("final.html", output=summary)


if __name__ == '__main__':
    app.run(debug=True)
