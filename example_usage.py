from client import QACorpusExtractor

corpus = (
    "Model Context Protocol is an open standard for connecting AI assistants to data and tools. "
    "In 2026, over 40 million developer agents adopted the standard worldwide."
)
qas = QACorpusExtractor.extract_all(corpus)
print(f"Extracted {len(qas)} QA pairs:")
for q in qas:
    print(f"- Q: {q['question']}\n  A: {q['answer']}")
