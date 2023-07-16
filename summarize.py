from transformers import PegasusForConditionalGeneration, PegasusTokenizer

# Initialize the Pegasus model and tokenizer outside the function
tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")


def generate_summary(text):

    # Encode the text using the tokenizer
    tokens = tokenizer.encode(
        text, truncation=True, padding="longest", return_tensors="pt")

    # Generate the summary for the text
    summary = model.generate(tokens, max_length=200)

    # Decode the summary and return it as the summarized text
    summarized_text = tokenizer.decode(
        summary[0], skip_special_tokens=True)

    return summarized_text
