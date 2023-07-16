from transformers import BartTokenizer, BartForConditionalGeneration

# Load the pre-trained BART model and tokenizer
model_name = 'facebook/bart-large-cnn'
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)


def generate_summary(text):
    # Tokenize the input text
    inputs = tokenizer([text], truncation=True, padding='longest',
                       max_length=1024, return_tensors='pt')

    # Generate the summary
    summary_ids = model.generate(
        inputs['input_ids'], num_beams=4, min_length=30, max_length=100, early_stopping=True)
    summary = [tokenizer.decode(g, skip_special_tokens=True,
                                clean_up_tokenization_spaces=False) for g in summary_ids]

    return summary[0]
