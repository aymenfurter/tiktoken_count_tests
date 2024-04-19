from azure.ai.resources._index._utils.tokens import token_length_function

def count_tokens(text, encoding="cl100k_base"):
    return token_length_function(encoding)(text)

sample_text = "hello world"

# Count the tokens
tokens_count = count_tokens(sample_text)
print(f"The number of tokens in the text '{sample_text}' is: {tokens_count}")
