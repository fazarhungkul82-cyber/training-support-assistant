from pypdf import PdfReader
from pathlib import Path

def load_all_sop():

    folder = Path("data/sop")

    all_text = ""

    for file in folder.glob("*.pdf"):

        reader = PdfReader(file)

        for page in reader.pages:

            text = page.extract_text()

            if text:
                all_text += f"\n\n=== {file.name} ===\n"
                all_text += text

    return all_text
