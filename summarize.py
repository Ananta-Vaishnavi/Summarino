from transformers import PegasusForConditionalGeneration, PegasusTokenizer

# Initialize the Pegasus model and tokenizer outside the function
tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")


def generate_summary(text):
    if len(text) > 5000:
        text = text[:5000]

    text_lines = text.split(".")
    summarized_text = ""

    for i in range(0, len(text_lines), 3):
        # Add the dot back when joining chunks
        chunk = ". ".join(text_lines[i:i+3])
        tokens = tokenizer.encode(
            chunk, truncation=True, padding="longest", return_tensors="pt")
        # Specify the desired summary length
        summary = model.generate(tokens, max_length=150)
        summarized_text += tokenizer.decode(
            summary[0], skip_special_tokens=True) + " "

    return summarized_text
