# Summarino

This project is a web-based text summarizer that utilizes the Transformers library and specifically the Pegasus model. The application is built using Flask as the backend framework and HTML, CSS, and JavaScript for the frontend.

## How it Works
The article summarizer utilizes advanced natural language processing techniques to condense lengthy articles into concise summaries. The summarization process involves several steps:

URL Summarization: If a URL is provided, the system retrieves the content from the specified link and extracts the main ideas and essential details from the article. This is done by analyzing the text, identifying important sentences, and constructing a summary that captures the essence of the article.

![See below](https://github.com/Ananta-Vaishnavi/Summarino/blob/main/images/URL_Summary.png)

Text Summarization: Alternatively, if no URL is provided, users can input their own text directly into the application. The system applies the same summarization techniques to the provided text, generating a summary that highlights the key points and crucial information.

![See below](https://github.com/Ananta-Vaishnavi/Summarino/blob/main/images/Text_summary.png)

## Functionality
Google's PEGASUS stands as a cutting-edge model in the field of abstractive text summarization. It leverages the gap-sentence generation pre-training self-supervised objective, specifically designed for Transformer encoder-decoder models, to enhance fine-tuning performance for abstractive summarization tasks. Notably, PEGASUS has achieved state-of-the-art results across a broad range of 12 diverse summarization datasets.

In the realm of abstractive single-document summarization evaluation, XSum emerges as a notable dataset. Its primary objective is to generate concise one-sentence summaries that succinctly answer the question, "What is the article about?" The dataset encompasses an extensive collection of 226,711 news articles, each accompanied by a corresponding one-sentence summary.

This project aims to showcase the capabilities of Google's PEGASUS model for abstractive text summarization and evaluate its performance using the XSum dataset. The main functionality of the project includes:

1. Abstractive Text Summarization: The project utilizes the PEGASUS model, a state-of-the-art abstractive summarization model, to generate concise summaries from given input text. It employs the Transformer encoder-decoder architecture and the gap-sentence generation self-supervised objective for improved fine-tuning performance.

2. XSum Dataset Evaluation: The project utilizes the XSum dataset, which consists of 226,711 news articles accompanied by one-sentence summaries. It evaluates the performance of the PEGASUS model by generating summaries for the articles and comparing them with the reference summaries provided in the dataset.

3. State-of-the-Art Results: The PEGASUS model has achieved state-of-the-art results on 12 diverse summarization datasets. This project aims to showcase its performance on the XSum dataset and demonstrate its effectiveness in generating accurate and concise summaries.

## Working

![See below](https://github.com/Ananta-Vaishnavi/Summarino/blob/main/images/pegasus.png)

- **Self-Supervised Objective for Pre-training:**
In the pre-training phase, several whole sentences are removed (masked) from documents, and the model is tasked with recovering these masked sentences. The objective is to output all the missing sentences concatenated together. This self-supervised task is challenging, as it requires the model to learn about language, general facts, and how to distill information from a document to generate a summary-like output. The advantage of self-supervision is that it allows the creation of many examples without human annotation, making it more scalable than purely supervised systems that require labeled data.

- **Identifying Important Sentences:**
To make the self-supervised examples even more similar to a summary, important sentences are identified to mask. These sentences are automatically selected by measuring their similarity to the rest of the document using a metric called ROUGE (Recall-Oriented Understudy for Gisting Evaluation). ROUGE computes n-gram overlaps between two texts and provides a score from 0 to 100, with higher scores indicating greater similarity.

- **Pre-training and Fine-Tuning:**
The model is pre-trained on a large corpus of web-crawled documents using the self-supervised gap-sentence generation objective. After pre-training, the model is fine-tuned on 12 diverse public abstractive summarization datasets, including news articles, scientific papers, patents, short stories, e-mails, legal documents, and how-to directions. Fine-tuning on these datasets leads to state-of-the-art results as measured by automatic metrics, surpassing the performance of other models with significantly fewer parameters.

- **Sample Efficiency in Fine-Tuning:**
One surprising finding is that the model does not require a large number of examples for fine-tuning. Even with only 1000 fine-tuning examples, the model performs better in most tasks than a strong baseline (Transformer encoder-decoder) using the full supervised data, which could have many orders of magnitude more examples. This "sample efficiency" lowers the scale and cost of supervised data collection, making the summarization model more accessible for various applications.

- **Human-Quality Summaries:**
Acknowledging that while automatic metrics like ROUGE are helpful for evaluating model performance, they don't provide a complete picture, particularly in terms of fluency and comparison to human performance. To address this, human evaluation is conducted, where human raters compare summaries generated by the model with human-written summaries without knowing which is which. The results show that the model's summaries are competitive with human ones, even when fine-tuned with only 1000 examples.

- **Test of Comprehension: Counting Ships:**
As a test of the model's abilities, an example from a summarization dataset and the model-generated abstractive summary are provided. The model successfully "counts" ships from 2 to 5, but when a sixth ship ("HMS Alphabet") is added, it miscounts it as "seven." This indicates the model's limited ability to generalize its counting, but it is still considered impressive as it was not explicitly programmed to count, showing some level of "symbolic reasoning" in the model.


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

## Conclusion
The article summarizer is a useful tool for quickly extracting the key points and main ideas from articles. Whether you have a specific URL or a piece of text that you want to summarize, this application utilizes advanced natural language processing techniques to generate concise and informative summaries. Feel free to modify and adapt the code to suit your specific needs and requirements. Happy summarizing!

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to submit a pull request. Checkout this out to get started [CONTRIBUTING.md](CONTRIBUTING.md)

## License
This project is licensed under the MIT License.
