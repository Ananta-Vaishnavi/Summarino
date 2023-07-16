# Summarino

This project is a web-based text summarizer that utilizes the Transformers library and specifically the BART (Bidirectional and AutoRegressive Transformers) model. The application is built using Flask as the backend framework and HTML, CSS, and JavaScript for the frontend.

## Functionality
Google's PEGASUS stands as a cutting-edge model in the field of abstractive text summarization. It leverages the gap-sentence generation pre-training self-supervised objective, specifically designed for Transformer encoder-decoder models, to enhance fine-tuning performance for abstractive summarization tasks. Notably, PEGASUS has achieved state-of-the-art results across a broad range of 12 diverse summarization datasets.

In the realm of abstractive single-document summarization evaluation, XSum emerges as a notable dataset. Its primary objective is to generate concise one-sentence summaries that succinctly answer the question, "What is the article about?" The dataset encompasses an extensive collection of 226,711 news articles, each accompanied by a corresponding one-sentence summary.

This project aims to showcase the capabilities of Google's PEGASUS model for abstractive text summarization and evaluate its performance using the XSum dataset. The main functionality of the project includes:

1. Abstractive Text Summarization: The project utilizes the PEGASUS model, a state-of-the-art abstractive summarization model, to generate concise summaries from given input text. It employs the Transformer encoder-decoder architecture and the gap-sentence generation self-supervised objective for improved fine-tuning performance.

2. XSum Dataset Evaluation: The project utilizes the XSum dataset, which consists of 226,711 news articles accompanied by one-sentence summaries. It evaluates the performance of the PEGASUS model by generating summaries for the articles and comparing them with the reference summaries provided in the dataset.

3. State-of-the-Art Results: The PEGASUS model has achieved state-of-the-art results on 12 diverse summarization datasets. This project aims to showcase its performance on the XSum dataset and demonstrate its effectiveness in generating accurate and concise summaries.

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
