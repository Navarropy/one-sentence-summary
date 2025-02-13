import os
import PyPDF2
import openai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def pdf_to_txt(pdf_path, txt_path):
    """Convert a PDF file to a TXT file."""
    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            text = ''.join(page.extract_text() or '' for page in reader.pages)
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)
        print(f"Converted {pdf_path} -> {txt_path}")
    except Exception as err:
        print(f"Error converting {pdf_path}: {err}")

def convert_all_pdfs(pdf_folder="files", txt_folder=os.path.join("files", "txt")):
    """Convert all PDF files in pdf_folder to TXT files in txt_folder."""
    os.makedirs(txt_folder, exist_ok=True)
    for file in os.listdir(pdf_folder):
        if file.lower().endswith(".pdf"):
            pdf_file = os.path.join(pdf_folder, file)
            txt_file = os.path.join(txt_folder, os.path.splitext(file)[0] + ".txt")
            if not os.path.exists(txt_file):
                pdf_to_txt(pdf_file, txt_file)

def summarize_text(text):
    """Generate a one-sentence summary of the text using OpenAI API."""
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes documents."},
                {"role": "user", "content": f"Please provide a concise summary, in a single sentence, of this text:\n\n{text}"}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as err:
        print(f"Error summarizing text: {err}")
        return None

def unique_summary_filename(stem, summary_folder):
    """Return a unique summary filename in summary_folder based on the file stem."""
    filename = f"{stem} - summary.txt"
    filepath = os.path.join(summary_folder, filename)
    counter = 1
    while os.path.exists(filepath):
        filename = f"{stem} - summary {counter}.txt"
        filepath = os.path.join(summary_folder, filename)
        counter += 1
    return filename

def create_summaries(txt_folder=os.path.join("files", "txt"), summary_folder=os.path.join("files", "summaries")):
    """Summarize all TXT files in txt_folder and save the summaries in summary_folder."""
    os.makedirs(summary_folder, exist_ok=True)
    for file in os.listdir(txt_folder):
        if file.lower().endswith(".txt"):
            txt_path = os.path.join(txt_folder, file)
            stem = os.path.splitext(file)[0]
            summary_file = os.path.join(summary_folder, unique_summary_filename(stem, summary_folder))
            if not os.path.exists(summary_file):
                with open(txt_path, 'r', encoding='utf-8') as f:
                    content = f.read()[:120000] + "\n\n[Content truncated due to length]"
                summary = summarize_text(content)
                if summary:
                    with open(summary_file, 'w', encoding='utf-8') as f:
                        f.write(summary)
                    print(f"Created summary: {summary_file}")

if __name__ == "__main__":
    convert_all_pdfs()    # Convert PDFs in 'files' to TXT in 'files/txt'
    create_summaries()    # Create summaries from TXT files in 'files/txt' and save in 'files/summaries'
