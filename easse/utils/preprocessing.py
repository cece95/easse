from functools import lru_cache
import sacrebleu
import sacremoses


@lru_cache(10**5)
def normalize(sentence, lowercase: bool = True, tokenizer: str = '13a', return_str: bool = True):
    if lowercase:
        sentence = sentence.lower()

    if tokenizer == "13a":
        normalized_sent = sacrebleu.tokenize_13a(sentence)
    elif tokenizer == "intl":
        normalized_sent = sacrebleu.tokenize_v14_international(sentence)
    elif tokenizer == "moses":
        normalized_sent = sacremoses.MosesTokenizer().tokenize(sentence, return_str=True)
    else:
        normalized_sent = sentence

    if not return_str:
        normalized_sent = normalized_sent.split()

    return normalized_sent
