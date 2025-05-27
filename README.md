
# Resume Checker 📄

Resume Checker is a simple Python tool that extracts **technical skills** from resumes in **PDF format**. It uses [spaCy](https://spacy.io/) for Natural Language Processing and `PyPDF2` to read the resume content. This tool helps job seekers or recruiters quickly identify relevant technical skills from a resume.

---

## 🚀 Features

- ✅ Extracts text from PDF resumes  
- ✅ Identifies technical skills using keyword matching  
- ✅ Uses Natural Language Processing (spaCy)  
- ✅ Easy to customize with more skills or features  

---

## 📂 Project Structure

```
resume-checker/
├── main.py         # Entry point - runs the resume checker
├── record.py       # Handles PDF reading and skill extraction
├── README.md       # This file
```

---

## 🔧 Requirements

- Python 3.7+
- `spaCy`
- `PyPDF2`

### Install dependencies

```bash
pip install spacy PyPDF2
python -m spacy download en_core_web_sm
```

---

## 📄 Usage

1. Place your resume PDF in a known directory.  
2. Update the file path in `main.py`:

```python
file_path = r'C:\Path\To\Your\Resume.pdf'
```

3. Run the script:

```bash
python main.py
```

You will see:
- The text content of the resume
- A list of extracted skills

---

## 🧠 Skills Detected

The tool currently looks for the following technical skills:

```
python, sql, pandas, nlp, machine learning,
java, javascript, c++, c#, html, css,
react, angular, vue, node.js, express, cloud computing,
docker, kubernetes, aws, azure, gcp, django,
git, github, bitbucket, jenkins, ci/cd, excel,
tableau, power bi, data visualization
```

You can extend the `SKILLS_KEYWORDS` set in `record.py` to include more!

---

## 📌 Future Improvements (TODO)

- Add a web interface   
- Include support for DOCX resumes  
- Use Named Entity Recognition (NER) for smarter skill extraction  
- Export results as CSV or JSON  

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open issues for suggestions or bugs.

---

## 👨‍💻 Author

**Ian Cliff Wende**  
https://github.com/iamiancliff
