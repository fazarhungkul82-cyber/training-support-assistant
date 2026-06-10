from pypdf import PdfReader
from pathlib import Path

def load_all_pdfs():

    docs = []

    folder = Path("data/sop")

    for pdf_file in folder.glob("*.pdf"):

        text = ""

        reader = PdfReader(pdf_file)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

        docs.append({
            "filename": pdf_file.name,
            "content": text
        })

    return docs


def retrieve_relevant_pdf(question):

    docs = load_all_pdfs()

    question = question.lower()

    best_score = 0
    best_doc = None

    for doc in docs:

        score = 0

        content = doc["content"].lower()

        for word in question.split():

            if word in content:
                score += 1

        if score > best_score:
            best_score = score
            best_doc = doc

    return best_doc
