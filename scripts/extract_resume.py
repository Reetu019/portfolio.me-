from pypdf import PdfReader
import sys
import pathlib

if len(sys.argv) < 2:
    print('Usage: extract_resume.py <pdf-path>')
    sys.exit(1)

pdf_path = pathlib.Path(sys.argv[1])
if not pdf_path.exists():
    print(f'ERROR: file not found: {pdf_path}')
    sys.exit(2)

reader = PdfReader(str(pdf_path))
text_parts = []
for i, page in enumerate(reader.pages):
    try:
        text = page.extract_text()
    except Exception as e:
        text = ''
    if text:
        text_parts.append(text)

full_text = "\n\n".join(text_parts)
out_path = pathlib.Path(__file__).parent / 'resume_text.txt'
try:
    out_path.write_text(full_text, encoding='utf-8')
    print(f'WROTE: {out_path}')
except Exception as e:
    print(f'ERROR_WRITING: {e}')
