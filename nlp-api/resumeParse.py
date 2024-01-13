import fitz
import nltk
from nltk.corpus import stopwords
from fuzzywuzzy import process, fuzz

nltk.download('stopwords')

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    return text

def fuzzy_match_skill(skill, skill_list):
    # Use fuzzywuzzy to find the best match in the skill list
    best_match, score = process.extractOne(skill, skill_list, scorer=fuzz.ratio)
    
    # Set a threshold for the match
    threshold = 85  # You can adjust this value based on your requirements
    
    if score >= threshold:
        return best_match
    else:
        return None

def extract_skills(text, hard_skills, soft_skills):
    words = nltk.word_tokenize(text.lower())  # Convert to lowercase for case-insensitive matching
    
    # Filter out common English stop words and short words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if len(word) > 2 and word.isalpha() and word not in stop_words]

    # Extract hard skills with a combination of exact and fuzzy matching
    extracted_hard_skills = [fuzzy_match_skill(skill, words) for skill in hard_skills]

    # Extract soft skills with a combination of exact and fuzzy matching
    extracted_soft_skills = [fuzzy_match_skill(skill, words) for skill in soft_skills]

    # Remove None values and duplicates from the lists
    extracted_hard_skills = list(set(filter(None, extracted_hard_skills)))
    extracted_soft_skills = list(set(filter(None, extracted_soft_skills)))

    return extracted_hard_skills, extracted_soft_skills

def generate_skills(path):
    pdf_path = path# nlp-api/resume3.pdf

    hard_skills_list = ['Python', 'Java', 'Machine Learning', 'Data Analysis', 
    'SQL', 'C++', 'JavaScript', 'HTML/CSS', 'C', 'Go', 'React', 'Vue', 'Angular', 'Haskell', 'Prolog', 'Heroku', 'AWS', 'Docker', 'Git', 'Scrum', 'Agile'
    'Jenkins', 'NLP', 'Excel', 'Word', 'Power Point', 'Microsoft Office', 'Linux', 'Github', 'Kubernetes', 'Elixir', 'Dart', 'Ruby', 'Rust', 'Kotlin', 
    'Cobol', 'Assembly', 'C#', '.NET', 'Nim', 'Matlab', 'CAD', 'Solidworks', 'Autodesk', 'Database Management', 'Tailwind', 'firebase', 'supabase', 'terraform']
    soft_skills_list = ['Communication', 'Teamwork', 'Problem Solving', 'Time Management', 'Adaptability', 'Leadership', 'Creativity', 'Conflict Resolution', 'Emotional Intelligence']

    resume_text = extract_text_from_pdf(pdf_path)
    hard_skills, soft_skills = extract_skills(resume_text, hard_skills_list, soft_skills_list)

    skills = hard_skills + soft_skills
    return skills

