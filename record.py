import spacy
import PyPDF2

nlp = spacy.load("en_core_web_sm")

SKILLS_KEYWORDS = {
    "python","sql","pandas","nlp","machine learning",
    "java","javascript","c++","c#","html","css",
    "react","angular","vue","node.js","express","cloud computing",
    "docker","kubernetes","aws","azure","gcp", "django",
    "git","github","bitbucket","jenkins","ci/cd","excel",
    "tableau","power bi","data visualization",
}

def read_pdf(file_path):
    """Read text from a PDF file."""
    if file_path.lower().endswith('.pdf'):
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() or ""
            return text
    else:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    

def extract_skills(text: str) -> set:
    """Extract skills from the text using keyword matching."""
    doc = nlp(text.lower())
    extracted = set()
   
    for token in doc:
        if token.text in SKILLS_KEYWORDS:
            extracted.add(token.text)

    return list(extracted)
