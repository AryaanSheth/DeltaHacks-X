import torch
from sentence_transformers import SentenceTransformer

# sentences = ["This is an example sentence", "Each sentence is converted"]

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language.",
    "Machine learning is transforming various industries.",
    "Artificial intelligence has the potential to revolutionize the future.",
    "Data science involves analyzing and interpreting complex data sets.",
    "Quantum computing is an exciting field with great potential.",
    "Natural language processing allows computers to understand and generate human language.",
    "Deep learning models are capable of capturing intricate patterns in data.",
    "Software development is a dynamic and rapidly evolving field.",
    "Blockchain technology is changing the landscape of finance and beyond.",
    "The fast colored wolf leaps over the tired hound"
]


model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

# Encode sentences directly using PyTorch
with torch.no_grad():  # Ensure no gradient is calculated during encoding
    embeddings = torch.tensor(model.encode(sentences))

# Calculate cosine similarity for each sentence with the first sentence
for i, sentence in enumerate(sentences[1:], start=1):
    similarity = torch.nn.functional.cosine_similarity(embeddings[0], embeddings[i], dim=0)
    print(f"Cosine Similarity between '{sentences[0]}' and '{sentence}': {similarity.item()} \n")
