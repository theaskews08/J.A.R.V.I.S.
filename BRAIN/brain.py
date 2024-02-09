from BRAIN.google_big_data import *
from BRAIN.google_small_data import *


def load_qa_data(file_path):
    qa_dict = {}
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(":")
            if len(parts) != 2:
                continue
            q, a = parts
            qa_dict[q] = a
    return qa_dict

qa_file_path = r"C:\Users\chatu\OneDrive\Desktop\J.A.R.V.I.S\DATA\qna.txt"
qa_dict = load_qa_data(qa_file_path)

def brain_cmd(text):
    if "jarvis" in text:
        text = text.replace("jarvis","")
        text = text.strip()
        if text in qa_dict:
            ans = qa_dict[text]
        elif "define" in text or "brief" in text or "research" in text or "teach me" in text:
           ans = deep_search(text)
        else:
            ans = search_brain(text)
        return ans

    else:
        pass






