"""Synthetic QA Pair Corpus Extractor.
100% Python Standard Library.
"""

import re

class QACorpusExtractor:
    """Extracts high-quality question-answer training pairs from unstructured text."""
    @staticmethod
    def extract_definition_qa(text: str) -> list:
        results = []
        sentences = re.split(r'(?<=[.!?])\s+', text)
        def_patterns = [
            r'^(?P<concept>[A-Z][\w\s-]{2,30}?)\s+is\s+(?:defined\s+as\s+|a\s+|an\s+|the\s+)?(?P<definition>.+)$',
            r'^(?P<concept>[A-Z][\w\s-]{2,30}?)\s+refers\s+to\s+(?P<definition>.+)$'
        ]
        for s in sentences:
            s_clean = s.strip()
            for pat in def_patterns:
                m = re.match(pat, s_clean, re.IGNORECASE)
                if m:
                    concept = m.group("concept").strip()
                    definition = m.group("definition").strip()
                    results.append({
                        "type": "definition",
                        "question": f"What is {concept}?",
                        "answer": f"{concept} is {definition}",
                        "source": s_clean
                    })
                    break
        return results

    @staticmethod
    def extract_factual_qa(text: str) -> list:
        results = []
        sentences = re.split(r'(?<=[.!?])\s+', text)
        for s in sentences:
            s_clean = s.strip()
            if re.search(r'\b\d{4}\b|\b\d+(?:\.\d+)?%\b|\b\d+\s+(?:million|billion|thousand|users|tokens|nodes)\b', s_clean):
                results.append({
                    "type": "factual_quantitative",
                    "question": f"What are the specific quantitative facts mentioned regarding this statement: '{s_clean[:60]}...'?",
                    "answer": s_clean,
                    "source": s_clean
                })
        return results

    @classmethod
    def extract_all(cls, text: str) -> list:
        return cls.extract_definition_qa(text) + cls.extract_factual_qa(text)
