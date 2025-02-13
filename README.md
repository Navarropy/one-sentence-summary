# PDF to TXT and Summaries

This project converts PDF files into TXT files and then generates a concise, one-sentence summary for each TXT file using the OpenAI API. The conversion and summary files are organized in dedicated folders.

## What It Does

- **PDF Conversion:**  
  Converts all PDF files in the `files` folder into TXT files. All TXT files are stored in the `files/txt` folder.

- **Summarization:**  
  Reads each TXT file from `files/txt`, generates a one-sentence summary using the OpenAI API, and saves the summary in the `files/summaries` folder. If duplicate summary file names occur, a counter is appended to the filename (e.g., `Book Name - summary.txt`, `Book Name - summary 1.txt`, etc.).

## Required Libraries

The following Python libraries are needed:

- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [openai](https://pypi.org/project/openai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

You can install them using pip:

```bash
pip install PyPDF2 openai python-dotenv
```

## Setup Instructions

1. **Create a `.env` File:**  
   In the root directory of the project, create a file named `.env` and add your OpenAI API key as follows:
   ```env
   OPENAI_API_KEY=your-api-key-here
   ```

2. **Prepare Your PDF Files:**  
   Place your PDF files into the `files` folder. The script will automatically convert them into TXT files in the `files/txt` folder. Run the script once and it will generate these folder automatically.

## How to Run

Simply run the main script:

```bash
python main.py
```

This will:
1. Convert all PDFs in the `files` folder to TXT files in the `files/txt` folder.
2. Generate one-sentence summaries for each TXT file and save them in the `files/summaries` folder.

## License
```
This project is licensed under the MIT License.
```
