from pathlib import Path
from pypdf import PdfReader

for path in Path("data/leases").glob("*.pdf"):
    print(path.name)
    reader = PdfReader(path)
    text = reader.pages[0].extract_text()
    print(text)