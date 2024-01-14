import torch
from sentence_transformers import SentenceTransformer
from resumeParse import generate_skills

def cosine_sim(path, ticket) -> float:

    skills_sentences = generate_skills('nlp-api/resume3.pdf', 'pdf')
    skills_text = ' '.join(skills_sentences)

    desc = generate_skills(ticket, "txt")
    desc_text = ' '.join(desc)

    combined_text = ' '.join(set((desc_text + skills_text).split()))

    model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

    # Encode sentences directly using PyTorch
    with torch.no_grad():  # Ensure no gradient is calculated during encoding
        # Encode the combined text
        embeddings = torch.tensor(model.encode(combined_text))

    # Convert desc and skills_sentences to PyTorch tensors
    desc_tensor = torch.tensor(model.encode(desc_text))
    skills_tensor = torch.tensor(model.encode(skills_text))

    # Calculate cosine similarity between the entire ticket description and skills
    similarity = torch.nn.functional.cosine_similarity(desc_tensor, skills_tensor, dim=0)
    return round(similarity.item(), 2)
