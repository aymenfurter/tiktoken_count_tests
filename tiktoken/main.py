import tiktoken

def count_tokens(text, encoding="cl100k_base"):
    encoder = tiktoken.get_encoding(encoding)
    # Encode the text
    encoded_text = encoder.encode(text)
    
    # Return the number of tokens
    return len(encoded_text)

# Sample text
sample_text = "hello world"

# Count the tokens
tokens_count = count_tokens(sample_text)
print(f"The number of tokens in the text '{sample_text}' is: {tokens_count}")
