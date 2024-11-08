import re

# Opening txt file
with open("Transformer.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
    print("Total number of characters in raw_text:", len(raw_text))
    print("raw_text for testing purpose:", raw_text[:100])

s_text = re.split(r"\s+|[.,;!?#]", raw_text)
print(s_text[:10])
print(len(s_text))

# Removing white space
s_text = [item for item in s_text if item.strip()]
print(s_text[:20])
pre_processed = s_text  # The process of cleaning and tokenizing is known as pre-processing

# Let's sort alphabetically to determine vocabulary size
all_words = sorted(set(pre_processed))
voc_size = len(all_words)
print("Size of Vocabulary:", voc_size)  # This is the size of vocabulary after cleaned

# After determining the vocabulary size we have to assign token id by creating dictionary
vocab = {token: integer for integer, token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break
print(type(vocab))  # After it processed by transformer we have to decode to reverse the process from token id to token to word

# Creating function to build tokenizer
class SimpleTokenizerV1():
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r"\s+|[.,;!?#]|--|\s", text)
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r"\s+([[.,;!?#])", r"\1", text)
        return text

# Initialize the tokenizer
tokenizer = SimpleTokenizerV1(vocab)
text = "how does transformer improves upon previous models like RNN?"
ids = tokenizer.encode(text)
print(ids)

# Decode
Decoded_text = tokenizer.decode(ids)
print(Decoded_text)


