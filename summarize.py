from transformers import PegasusForConditionalGeneration, PegasusTokenizer

# Initialize the Pegasus model and tokenizer outside the function
tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")


def generate_summary(text):
    if len(text) > 5000:
        text = text[:5000]

    tokens = tokenizer.encode(
        text, truncation=True, padding="longest", return_tensors="pt")
    # Specify the desired summary length
    summary = model.generate(tokens, max_length=150)
    summarized_text = tokenizer.decode(
        summary[0], skip_special_tokens=True)

    return summarized_text


text = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule. Python is dynamically typed and garbage-collected."""
print(generate_summary(text))
