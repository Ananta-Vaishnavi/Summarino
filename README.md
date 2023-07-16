# Summarino

This project is a web-based text summarizer that utilizes the Transformers library and specifically the BART (Bidirectional and AutoRegressive Transformers) model. The application is built using Flask as the backend framework and HTML, CSS, and JavaScript for the frontend.

## Functionality

The summarizer takes a block of text as input and generates a concise summary of the text using the BART model. The BART model is a state-of-the-art language generation model that has been trained on a large corpus of data and is capable of producing high-quality summaries.

## Working



## Getting Started

To set up the project, follow these steps:

1. Clone the Repository:

```
git clone https://github.com/Ananta-Vaishnavi/Summarino.git
```

2. Create and Activate a Virtual Environment:

```
cd Summarino
python -m venv venv
source venv/bin/activate  # For Unix/Linux
venv\Scripts\activate  # For Windows
```

3. Install Dependencies:
```
pip install -r requirements.txt
```

4. Run the Flask Application:
```
flask run --host 0.0.0.0 --port 5010
```

## Usage
Once the Flask application is running, open your web browser and navigate to `http://localhost:5000` to access the summarizer interface. Enter the text you want to summarize and click the "Summarize" button. The generated summary will be displayed on the screen.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to submit a pull request. Checkout this out to get started [CONTRIBUTING.md](CONTRIBUTING.md)

## License
This project is licensed under the MIT License.
