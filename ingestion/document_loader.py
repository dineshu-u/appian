import PyPDF2
import os

def load_policy_documents(folder_path):
    policy_chunks = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, file_name)
            reader = PyPDF2.PdfReader(pdf_path)

            for page_number, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    policy_chunks.append({
                        "document": file_name,
                        "page": page_number + 1,
                        "text": text.strip()
                    })

    return policy_chunks
