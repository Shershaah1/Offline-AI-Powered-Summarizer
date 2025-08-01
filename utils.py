import os
import torch
from transformers import BartTokenizer, BartForConditionalGeneration
from docx import Document
from PyPDF2 import PdfReader

# Load Facebook BART Large CNN Model from local 'model' folder
tokenizer = BartTokenizer.from_pretrained("model")
model = BartForConditionalGeneration.from_pretrained("model")

def extract_text(file_path):
    ext = file_path.split('.')[-1].lower()
    text = ""

    if ext == "pdf":
        reader = PdfReader(file_path)
        text = "\n".join(page.extract_text() or "" for page in reader.pages)

    elif ext == "docx":
        doc = Document(file_path)
        text = "\n".join(p.text for p in doc.paragraphs)

    elif ext == "txt":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    return text

def determine_chunking_strategy(text):
    num_words = len(text.split())
    approx_pages = num_words // 300  # assuming avg 300 words per page

    if approx_pages <= 50:
        return 300  # smaller chunks (more detail)
    elif approx_pages <= 120:
        return 600  # medium chunks
    else:
        return 1000  # large chunks (faster)

def split_into_chunks(text, max_tokens):
    words = text.split()
    chunks = []

    while words:
        chunk_words = words[:max_tokens]
        chunks.append(" ".join(chunk_words))
        words = words[max_tokens:]

    return chunks

def summarize_chunk(chunk):
    cleaned = chunk.replace('\n', ' ').strip()
    inputs = tokenizer([cleaned], return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs.input_ids, max_length=180, min_length=60, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def extract_and_summarize(file_path):
    text = extract_text(file_path)
    chunk_size = determine_chunking_strategy(text)
    chunks = split_into_chunks(text, max_tokens=chunk_size)

    final_summary = ""
    for chunk in chunks:
        summary = summarize_chunk(chunk)
        final_summary += summary + "\n\n"

    return final_summary.strip()
