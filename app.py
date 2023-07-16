from flask import Flask, render_template, request, jsonify
from summarize import generate_summary
from web_extract import extract_data_from_webpage

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/summarize', methods=['POST'])
def summarize():
    if request.form.get('articleURL'):
        article_url = request.form['articleURL']
        article_text = extract_data_from_webpage(article_url)
        summary = generate_summary(article_text)
    elif request.form.get('articleText'):
        summary = generate_summary(request.form['articleText'])
    else:
        return jsonify({'error': 'Invalid request'})

    return jsonify({'summary': summary})


if __name__ == '__main__':
    app.run(debug=True)
