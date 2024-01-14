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

# test = """
# Ticket Title: Enhance User Profile Management Module

# Descripti

# Objective:
# Improve the existing User Profile Management module to provide a more intuitive and personalized experience for our users.

# Details:

# Technical Enhancements:

# User Profile Page:

# Implement dynamic rendering of user profiles with HTML, CSS, and JavaScript to enhance the visual presentation.
# Integrate responsive design principles for a seamless user experience across devices.
# Utilize AJAX for asynchronous data loading to improve page load times.
# Skills Display:

# Enhance the skills section to dynamically showcase a user's proficiency in coding languages such as Python, JavaScript, and Java.
# Implement a tag-based system for easy categorization and display of technical skills.
# Integration with External APIs:

# Explore and integrate relevant external APIs (e.g., GitHub API) to automatically fetch and display a user's latest coding projects and contributions.
# Ensure secure handling of API keys and data privacy.
# Soft Skills Integration:

# Communication:

# Implement a user-friendly interface to allow users to input and showcase their soft skills such as communication, teamwork, and leadership.
# Provide a rating system or descriptive input for users to self-assess their soft skills.
# User Feedback Mechanism:

# Introduce a user feedback mechanism to collect testimonials or endorsements from colleagues, mentors, or project collaborators.
# Display aggregated feedback on the user profile in a visually appealing format.
# Acceptance Criteria:

# User profiles are visually enhanced with HTML, CSS, and JavaScript.
# Coding languages and technical skills are dynamically displayed and categorized.
# External APIs fetch and display relevant coding projects on the user profile.
# Soft skills are incorporated into the user profile, allowing self-assessment and display.
# User feedback mechanism is implemented and testimonials are displayed on the user profile.
# Code is well-documented, modular, and adheres to coding standards.
# Notes:

# Collaborate with the UX/UI team for design considerations.
# Ensure compatibility with various browsers and devices.
# Conduct thorough testing to validate the functionality and performance improvements.

# """

# print(cosine_sim('nlp-api/resume3.pdf', test))