import spacy

nlp = spacy.load("en_core_web_sm")
resume_text = "John Doe, Python Developer, 5 years experience."
doc = nlp(resume_text)

for ent in doc.ents:
    print(ent.text, "-", ent.label_)
