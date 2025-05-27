from record import read_pdf, extract_skills

def main():
    file_path = r'C:\Users\HP\Desktop\Ian Docs\Ian_Resume_.pdf'
    resume_text = read_pdf(file_path)
    print("\n ===== Resume Text Content =====")
    print(resume_text)

    print("\n ===== Extracted Skills =====")
    skills = extract_skills(resume_text)    
    print(skills)

# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()